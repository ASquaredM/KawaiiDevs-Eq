import UI
import wave
#import untitled
from PyQt5 import QtWidgets, QtCore
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import sys
from GetDataFromFile import getWavData
import scipy
import scipy.io as sio
import scipy.fftpack as fftpk
import sounddevice as sd
import cmath
import Colors
from PopUpWindowClass import Ui_PopUpWindow
from WinFns import WinFn
#import 

#WinFn(Win_Fn,freq,Bands,Gains,data)

#Init a gain for each band
Gains = np.ones(10)

#Freq. Spectrum Division (Setting Bands)
Bands = np.array([[20,40],[40,80],[80,160]
                    ,[160,300],[300,600],[600,1200]
                    ,[1200,2400],[2400,5000],[5000,10000]
                    ,[10000,20000]])

#Supported Window Functions
Win_Fn = np.array(['Rectangular','Hamming','Hanning'])

#Saving Modes#
SaveMode=np.array(["To A File","Save1","Save2"])


class ApplicationWindow(UI.Ui_MainWindow):
    def __init__(self,mainWindow):
        super(ApplicationWindow,self).setupUi(mainWindow)
        self.VariableInitialization()
        self.ButtonInitialization()
        self.sliderInitialization()

    def VariableInitialization(self):
        self.slidersEnable=False
        self.PopUpMenuIsON=False
        self.FileName=None
        self.Path=None
        self.freqs=None 
        self.FFTdata=None
        self.SampleRate=None
        self.MainData=[self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path]
        self.SavedData1=None
        self.SavedData2=None
        self.OpenedData=None
            
    def ButtonInitialization(self):
        self.OpenFileButton.clicked.connect(self.OpenFile)
        self.OpenFileButton.clicked.connect(self.graphMainData)
        self.PlayButton.clicked.connect(self.generateSound)
        self.PauseButton.clicked.connect(self.pauseSound)
        self.SaveButton.clicked.connect(self.saveSoundFile)
        self.CompareButton.clicked.connect(self.OpenPopUpWindow)
        self.OnOff.clicked.connect(self.slidersChangeState)

    def OpenFile(self):
        Output = self.getData()
        if Output is not None:
            [self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path]= Output
            self.UpdateMainData()
            self.OpenedData=self.MainData

    def getData(self):
        #to stop playing the old music#
        if self.FFTdata is not None:
            sd.stop()
        #get the Data#
        return getWavData()

    def UpdateMainData(self):
        self.MainData=[self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path]

    def updateEqualizedData(self):
        self.MainData=self.OpenedData
        [self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path]=self.MainData

    def graphMainData(self):
        if self.FFTdata is not None:
            self.graph(self.FFTdata,self.freqs,Colors.white)

    def graph(self,data,freqs,color):
        if self.FFTdata is not None:
            self.widget.plotItem.clear()
            self.widget.plotItem.plot(freqs[range(len(data)//2)],abs(data[range(len(data)//2)]),pen =color )
            #self.widget.plotItem.plot(freqs,abs(data),pen =color)


    def generateSound(self):
        if self.FFTdata is not None:
            generatedAudio=np.real(fftpk.ifft(self.FFTdata))
            sd.play(generatedAudio,self.SampleRate)
            
    def pauseSound(self):
        if (self.FFTdata is not None):
            sd.stop()
    
    def saveSoundFile(self):
        if self.FFTdata is not None:
            indexOfSaveModes=self.SaveMode.currentIndex()
            if SaveMode[indexOfSaveModes]=="To A File":
                GenratedAudio=np.real(fftpk.ifft(self.FFTdata))
                SavedData=GenratedAudio
                name= QtGui.QFileDialog.getSaveFileName( None,'Save File',self.Path+".wav")[0]
                #print(name,self.SampleRate,SavedData)
                sio.wavfile.write(name, self.SampleRate, SavedData)
            if SaveMode[indexOfSaveModes]=="Save1":
                self.SavedData1=self.MainData
            if SaveMode[indexOfSaveModes]=="Save2":
                self.SavedData2=self.MainData

    def OpenPopUpWindow(self):
        if self.FFTdata is not None:
            print("Opening a new popup window...")
            self.mainWindow=QtWidgets.QMainWindow()
            self.PopUp = Ui_PopUpWindow(self.mainWindow,self.MainData,self.SavedData1,self.SavedData2)
            self.mainWindow.show()



    def sliderInitialization(self):

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

        self.slidersEnable=False
        self.OnOff.setText("ON")

        self.sliders[0].valueChanged.connect(lambda :self.edittingSliderValue(0))
        self.sliders[1].valueChanged.connect(lambda :self.edittingSliderValue(1))
        self.sliders[2].valueChanged.connect(lambda :self.edittingSliderValue(2))
        self.sliders[3].valueChanged.connect(lambda :self.edittingSliderValue(3))
        self.sliders[4].valueChanged.connect(lambda :self.edittingSliderValue(4))
        self.sliders[5].valueChanged.connect(lambda :self.edittingSliderValue(5))
        self.sliders[6].valueChanged.connect(lambda :self.edittingSliderValue(6))
        self.sliders[7].valueChanged.connect(lambda :self.edittingSliderValue(7))
        self.sliders[8].valueChanged.connect(lambda :self.edittingSliderValue(8))
        self.sliders[9].valueChanged.connect(lambda :self.edittingSliderValue(9))

        self.ApplyEqualizerButton.clicked.connect(self.ApplyEqualizer)

        
        for numberOfBand in range(0,10):
            self.sliders[numberOfBand].setRange(0,100)
            self.sliders[numberOfBand].setValue(50)
            self.sliders[numberOfBand].setDisabled(True)
            #self.sliders[numberOfBand].valueChanged.connect(lambda :self.edittingSliderValue(numberOfBand))

    def slidersChangeState(self):
        if self.FFTdata is not None:
            if self.slidersEnable==False:
                for numberOfBand in range(0,10):
                    self.sliders[numberOfBand].setEnabled(True)
                self.slidersEnable=True
                self.OnOff.setText("OFF")
            else:
                for numberOfBand in range(0,10):
                    self.sliders[numberOfBand].setDisabled(True)
                    self.sliders[numberOfBand].setValue(50)
                self.slidersEnable=False
                self.OnOff.setText("ON")

    def edittingSliderValue(self,numberOfBand): 
        Gains[numberOfBand] = self.sliders[numberOfBand].value()/50

    def ApplyEqualizer(self):
        windowMode=Win_Fn[self.WindowMode.currentIndex()]
        self.updateEqualizedData()
        #print(self.FFTdata)
        #print(self.freqs)
        self.FFTdata,self.freqs=WinFn(windowMode,self.freqs,Bands,Gains,self.FFTdata)
        self.UpdateMainData()
        self.graphMainData()
        
        

        
def main():
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

