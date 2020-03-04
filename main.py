import UI
import wave
#import untitled
from PyQt5 import QtWidgets, QtCore
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import sys
from GetDataFromFile import getDataFromAFile
import scipy
import scipy.io as sio
import scipy.fftpack as fftpk
import sounddevice as sd
import cmath


class ApplicationWindow(UI.Ui_MainWindow):
    def __init__(self,mainWindow):
        super(ApplicationWindow,self).setupUi(mainWindow)
        
        self.oneChannelData=None
        self.FileName=None
        self.Path=None
        self.FFT=None
        self.freqs=None 
        self.oneChannelData=None

        self.OpenFileButton.clicked.connect(self.getData)
        self.OpenFileButton.clicked.connect(self.graph)
        self.PlayButton.clicked.connect(self.generateSound)
        self.PauseButton.clicked.connect(self.pauseSound)
        self.SaveButton.clicked.connect(self.saveSoundFile)
        
    def getData(self):
        #get the file and read it#
        self.filePath=QtWidgets.QFileDialog.getOpenFileName(None,  'load', "./","All Files *;;" "*.wav;;" " *.mp3;;" "*.snd")
        dataFromTheFile=getDataFromAFile(self.filePath)
        Output,self.FileName,self.Path = dataFromTheFile if dataFromTheFile is not None  else  [None,self.FileName]
        if Output is not None:
            nChannelData,self.SampleRate=Output
            print(isinstance( nChannelData[0] ,np.ndarray))
            if  isinstance( nChannelData[0] ,np.ndarray):
                self.oneChannelData=nChannelData[:,0]
            else:
                self.oneChannelData=nChannelData
            self.graph()
        
    def graph(self):
        if self.oneChannelData is not None:
            self.FFT=fftpk.fft(self.oneChannelData)
            self.freqs =fftpk.fftfreq(len(self.FFT),(1.0/self.SampleRate))
            self.widget.plotItem.plot(self.freqs[range(len(self.FFT)//2)],abs(self.FFT[range(len(self.FFT)//2)]))
    
    
    def generateSound(self):
        if self.oneChannelData is not None:
            generatedAudio=np.real(fftpk.ifft(self.FFT))
            sd.play(generatedAudio,self.SampleRate)
            
    def pauseSound(self):
        if (self.oneChannelData is not None):
            sd.stop()
    
    def saveSoundFile(self):
        
        if self.oneChannelData is not None:
            GenratedAudio=np.real(fftpk.ifft(self.FFT))
            SavedData=GenratedAudio
            name= QtGui.QFileDialog.getSaveFileName( None,'Save File',self.Path+".wav")[0]
            print(name,self.SampleRate,SavedData)
            sio.wavfile.write(name, self.SampleRate, SavedData)
        #getOpenFileName(None,  'load', "./","All Files *;;" "*.wav;;" " *.mp3;;" "*.snd")
            
            
        
def main():
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ui=ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

