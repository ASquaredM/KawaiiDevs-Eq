import UI
import wave
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
        
        self.data=None
        self.FileName=None
        self.Path=None
        self.FFT=None
        self.freqs=None 
        
        self.OpenFileButton.clicked.connect(self.getData)
        self.OpenFileButton.clicked.connect(self.graph)
        self.PlayButton.clicked.connect(self.generateSound)
        self.PauseButton.clicked.connect(self.pauseSound)
        self.SaveButton.clicked.connect(self.saveSoundFile)
        
        #Init a gain for each band
        self.Gains = np.ones([10])

        #Freq. Spectrum Division (Setting Bands)
        self.Bands = np.array([[20,40],[40,80],[80,160]
                            ,[160,300],[300,600],[600,1200]
                            ,[1200,2400],[2400,5000],[5000,10000]
                            ,[10000,20000]])
        
        #Supported Window Functions
        self.Win_Fn = np.array(['Rectangular','Hamming','Hanning'])
        
    def getData(self):
        #get the file and read it#
        self.filePath=QtWidgets.QFileDialog.getOpenFileName(None,  'load', "./","All Files *;;" "*.wav;;" " *.mp3;;" "*.snd")
        dataFromTheFile=getDataFromAFile(self.filePath)
        Output,self.FileName,self.Path = dataFromTheFile if dataFromTheFile is not None  else  [None,self.FileName]
        if Output is not None:
            print(self.data)
            self.data,self.SampleRate=Output
            print(len(self.data)*0.00095437989)
            realData=self.data[:,0]
            imagData=self.data[:,1]
            self.complexData=realData + 1j * imagData #np.vectorize(complex)(realData*1000, imagData)
            self.graph()
        
    def graph(self):
        if self.data is not None:
            self.FFT=fftpk.fft(self.complexData)
            self.freqs =fftpk.fftfreq(len(self.FFT),(1.0/self.SampleRate))
            self.widget.plotItem.plot(self.freqs[range(len(self.FFT)//2)],abs(self.FFT[range(len(self.FFT)//2)]))
            self.IFFT=fftpk.ifft(self.FFT)

    
    
    def generateSound(self):
        if self.data is not None:
            generatedAudio=np.real(fftpk.ifft(self.FFT))
            sd.play(generatedAudio,self.SampleRate)
            
    def pauseSound(self):
        if (self.data is not None):
            sd.stop()
    
    def saveSoundFile(self):
        if self.data is not None:
            GenratedAudio=fftpk.ifft(self.FFT)
            GenratedAudio=np.real(GenratedAudio)
            """SavedData=([],self.SampleRate)
            for frame in GenratedAudio:
                SavedData[0].extend([[np.real(frame),np.imag(frame)]])
            print(SavedData)
            SavedData=np.array(SavedData[0][:,0])"""
            SavedData=GenratedAudio
            name= QtGui.QFileDialog.getSaveFileName( None,'Save File',self.Path+".wav")[0]
            print(name,self.SampleRate,SavedData)
            sio.wavfile.write(name, self.SampleRate//2, SavedData.astype(np.dtype('i2')))
            """wf = wave.open(name, 'wb')
            #wf.setnchannels(channels)
            duration=3
            wf.setsampwidth(3)
            wf.setframerate(self.SampleRate)
            GenratedAudio=fftpk.ifft(self.FFT)
            SavedData=[]
            for frame in GenratedAudio:
                SavedData.extend([[np.real(frame),np.imag(frame)]])
            wf.setnframes(int(self.SampleRate * duration))
            wf.writeframes(SavedData)
            wf.close()"""
        #getOpenFileName(None,  'load', "./","All Files *;;" "*.wav;;" " *.mp3;;" "*.snd")
            
            
        
def main():
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ui=ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()