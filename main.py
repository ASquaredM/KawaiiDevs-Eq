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
import Colors

#Init a gain for each band
Gains = np.ones([10])

#Freq. Spectrum Division (Setting Bands)
Bands = np.array([[20,40],[40,80],[80,160]
                    ,[160,300],[300,600],[600,1200]
                    ,[1200,2400],[2400,5000],[5000,10000]
                    ,[10000,20000]])

#Supported Window Functions
Win_Fn = np.array(['Rectangular','Hamming','Hanning'])


class ApplicationWindow(UI.Ui_MainWindow):
    def __init__(self,mainWindow):
        super(ApplicationWindow,self).setupUi(mainWindow)
        
        self.oneChannelData=None
        self.FileName=None
        self.Path=None
        self.FFT=None
        self.freqs=None 
        self.data=None
        self.SampleRate=None

        self.OpenFileButton.clicked.connect(self.OpenFile)
        self.OpenFileButton.clicked.connect(self.graphMainData)
        self.PlayButton.clicked.connect(self.generateSound)
        self.PauseButton.clicked.connect(self.pauseSound)
        self.SaveButton.clicked.connect(self.saveSoundFile)
        self.CompareButton.clicked.connect(self.compareToAFile)
        self.ClearComparedButton.clicked.connect(self.ClearComparedButton)

    def OpenFile(self):
        [self.data,self.freqs,self.SampleRate,self.FileName,self.Path]= self.getData()

    def getData(self):

        if self.data is not None:
            sd.stop()
        #get the file and read it#
        filePath=QtWidgets.QFileDialog.getOpenFileName(None,  'load', "./","All Files *;;" "*.wav;;" " *.mp3;;" "*.snd")
        dataFromTheFile=getDataFromAFile(filePath)
        Output,FileName,Path = dataFromTheFile if dataFromTheFile is not None  else  [None,self.FileName,self.Path]
        if Output is not None:
            nChannelData,SampleRate=Output
            print(isinstance( nChannelData[0] ,np.ndarray))
            if  isinstance(nChannelData[0] ,np.ndarray):
                oneChannelData=nChannelData[:,0]
            else:
                oneChannelData=nChannelData
            FFTData=fftpk.fft(oneChannelData)
            freqs =fftpk.fftfreq(len(FFTData),(1.0/SampleRate))
            print(FFTData,freqs,SampleRate,FileName,Path)
            return FFTData,freqs,SampleRate,FileName,Path

    def graphMainData(self):
        if self.data is not None:
            self.graph(self.data,self.freqs,Colors.white)

    def graph(self,data,freqs,color):
        if self.data is not None:
            self.widget.plotItem.plot(freqs[range(len(data)//2)],abs(data[range(len(data)//2)]),pen =color )
    
    
    def generateSound(self):
        if self.data is not None:
            generatedAudio=np.real(fftpk.ifft(self.data))
            sd.play(generatedAudio,self.SampleRate)
            
    def pauseSound(self):
        if (self.data is not None):
            sd.stop()
    
    def saveSoundFile(self):
        if self.data is not None:
            GenratedAudio=np.real(fftpk.ifft(self.data))
            SavedData=GenratedAudio
            name= QtGui.QFileDialog.getSaveFileName( None,'Save File',self.Path+".wav")[0]
            print(name,self.SampleRate,SavedData)
            sio.wavfile.write(name, self.SampleRate, SavedData)

    def compareToAFile(self):
        if self.data is not None:
            [data,freqs,SampleRate,FileName,Path]= self.getData()
            self.graph(data,freqs,color=Colors.red)
            self.graphMainData()
    
    def clearCompared(self):
        if self.data is not None:
            self.widget.plotItem.clear()
            self.widget.plotItem.plot(self.freqs[range(len(self.data)//2)],abs(self.data[range(len(self.data)//2)]),pen =Colors.white )

            
            
        
def main():
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ui=ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

