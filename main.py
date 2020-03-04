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


#WinFn(Win_Fn,freq,Bands,Gains,data)

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
        
        self.FileName=None
        self.Path=None
        self.freqs=None 
        self.FFTdata=None
        self.SampleRate=None

        self.OpenFileButton.clicked.connect(self.OpenFile)
        self.OpenFileButton.clicked.connect(self.graphMainData)
        self.PlayButton.clicked.connect(self.generateSound)
        self.PauseButton.clicked.connect(self.pauseSound)
        self.SaveButton.clicked.connect(self.saveSoundFile)
        self.CompareButton.clicked.connect(self.compareToAFile)
        self.ClearComparedButton.clicked.connect(self.clearCompared)

        self.sliders=[
            self.Band1Slider,
            self.Band2Slider,
            self.Band3Slider,
            self.Band4Slider,
            self.Band5Slider,
            self.Band6Slider,
            self.Band7Slider,
            self.Band8Slider,
            self.Band9Slider,
            self.Band10Slider
        ]
        

    def OpenFile(self):
        Output = self.getData()
        if Output is not None:
            [self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path]= Output

    def getData(self):
        #to stop playing the old music#
        if self.FFTdata is not None:
            sd.stop()
        #get the file and read it#
        filePath=QtWidgets.QFileDialog.getOpenFileName(None,  'load', "./","All Files *;;" "*.wav;;" " *.mp3;;" "*.snd")
        dataFromTheFile=getDataFromAFile(filePath)
        if dataFromTheFile is not None:
            Output,FileName,Path = dataFromTheFile if dataFromTheFile is not None  else  [None,self.FileName,self.Path]
            nChannelData,SampleRate=Output
            if  isinstance(nChannelData[0] ,np.ndarray):
                oneChannelData=nChannelData[:,0]
            else:
                oneChannelData=nChannelData
            FFTData=fftpk.fft(oneChannelData)
            freqs =fftpk.fftfreq(len(FFTData),(1.0/SampleRate))
            print(FFTData,freqs,SampleRate,FileName,Path)
            return FFTData,freqs,SampleRate,FileName,Path
        else:
            return None

    def graphMainData(self):
        if self.FFTdata is not None:
            self.graph(self.FFTdata,self.freqs,Colors.white)

    def graph(self,data,freqs,color):
        if self.FFTdata is not None:
            self.widget.plotItem.plot(freqs[range(len(data)//2)],abs(data[range(len(data)//2)]),pen =color )
    
    
    def generateSound(self):
        if self.FFTdata is not None:
            generatedAudio=np.real(fftpk.ifft(self.FFTdata))
            sd.play(generatedAudio,self.SampleRate)
            
    def pauseSound(self):
        if (self.FFTdata is not None):
            sd.stop()
    
    def saveSoundFile(self):
        if self.FFTdata is not None:
            GenratedAudio=np.real(fftpk.ifft(self.FFTdata))
            SavedData=GenratedAudio
            name= QtGui.QFileDialog.getSaveFileName( None,'Save File',self.Path+".wav")[0]
            print(name,self.SampleRate,SavedData)
            sio.wavfile.write(name, self.SampleRate, SavedData)

    def compareToAFile(self):
        if self.FFTdata is not None:
            [data,freqs,SampleRate,FileName,Path]= self.getData()
            self.graph(data,freqs,color=Colors.red)
            self.graphMainData()
    
    def clearCompared(self):
        if self.FFTdata is not None:
            self.widget.plotItem.clear()
            self.graphMainData()

    """def ChangeSlider(self):
        if self.data is not None:"""
            
            

            
            
        
def main():
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ui=ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

