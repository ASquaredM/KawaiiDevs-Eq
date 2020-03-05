<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
import UI
import wave
#import untitled
from PyQt5 import QtWidgets, QtCore
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import sys
<<<<<<< HEAD
from GetDataFromFile import getDataFromAFile
=======
from GetDataFromFile import getWavData
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
import scipy
import scipy.io as sio
import scipy.fftpack as fftpk
import sounddevice as sd
import cmath
import Colors
<<<<<<< HEAD
from PopUpWindowClass import BuildPopUpWindow
=======
from PopUpWindowClass import Ui_PopUpWindow
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions
=======
from WinFns import WinFn
>>>>>>> 33d840c... master
=======
from WinFns import WinFn
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
#import 

#WinFn(Win_Fn,freq,Bands,Gains,data)

#Init a gain for each band
<<<<<<< HEAD
Gains = [0,0,0,0,0,0,0,0,0,0]
=======
Gains = np.ones(10)
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6

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
<<<<<<< HEAD
        self.SavedData1=[]
        self.SavedData2=[]
=======
        self.SavedData1=None
        self.SavedData2=None
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
            
    def ButtonInitialization(self):
        self.OpenFileButton.clicked.connect(self.OpenFile)
        self.OpenFileButton.clicked.connect(self.graphMainData)
        self.PlayButton.clicked.connect(self.generateSound)
        self.PauseButton.clicked.connect(self.pauseSound)
        self.SaveButton.clicked.connect(self.saveSoundFile)
        self.CompareButton.clicked.connect(self.OpenPopUpWindow)
<<<<<<< HEAD
        #self.CompareButton.clicked.connect(self.compareToAFile)
        #self.ClearComparedButton.clicked.connect(self.clearCompared)
=======
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
        self.OnOff.clicked.connect(self.slidersChangeState)

    def OpenFile(self):
        Output = self.getData()
        if Output is not None:
            [self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path]= Output
<<<<<<< HEAD
            print(self.MainData)
            print(self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path)
=======
            self.UpdateMainData()
<<<<<<< HEAD

<<<<<<< HEAD
    def UpdateMainData(self):
        self.MainData=[self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path]
>>>>>>> ef09d7a... PopUp Functions
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6

=======
>>>>>>> 33d840c... master
    def getData(self):
        #to stop playing the old music#
        if self.FFTdata is not None:
            sd.stop()
<<<<<<< HEAD
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
=======
        #get the Data#
        return getWavData()
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions

    def UpdateMainData(self):
        self.MainData=[self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path]
=======

    def UpdateMainData(self):
        self.MainData=[self.FFTdata,self.freqs,self.SampleRate,self.FileName,self.Path]
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6

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
            indexOfSaveModes=self.SaveMode.currentIndex()
            if SaveMode[indexOfSaveModes]=="To A File":
                GenratedAudio=np.real(fftpk.ifft(self.FFTdata))
                SavedData=GenratedAudio
                name= QtGui.QFileDialog.getSaveFileName( None,'Save File',self.Path+".wav")[0]
                print(name,self.SampleRate,SavedData)
                sio.wavfile.write(name, self.SampleRate, SavedData)
            if SaveMode[indexOfSaveModes]=="Save1":
                self.SavedData1=self.MainData
            if SaveMode[indexOfSaveModes]=="Save2":
                self.SavedData2=self.MainData

    def OpenPopUpWindow(self):
<<<<<<< HEAD
        BuildPopUpWindow(self.MainData,self.SavedData1,self.SavedData2)
        




    def compareToAFile(self):
        if self.FFTdata is not None:
            [data,freqs,SampleRate,FileName,Path]= self.getData()
            self.graph(data,freqs,color=Colors.red)
            self.graphMainData()
    
    def clearCompared(self):
        if self.FFTdata is not None:
            self.widget.plotItem.clear()
            self.graphMainData()
=======
        if self.FFTdata is not None:
            print("Opening a new popup window...")
            self.mainWindow=QtWidgets.QMainWindow()
            self.PopUp = Ui_PopUpWindow(self.mainWindow,self.MainData,self.SavedData1,self.SavedData2)
            self.mainWindow.show()
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6



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

<<<<<<< HEAD
        self.ApplyEqualizerButton.clicked.connect(self.ApplyEqualizer)

=======
<<<<<<< HEAD
=======
        self.ApplyEqualizerButton.clicked.connect(self.ApplyEqualizer)

>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
        
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
<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
                windowMode=Win_Fn[self.WindowMode.currentIndex()]
                print(windowMode)
<<<<<<< HEAD
                self.WindowMode.setDisabled(True)
=======
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions
=======
>>>>>>> 33d840c... master
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
                self.slidersEnable=True
                self.OnOff.setText("OFF")
            else:
                for numberOfBand in range(0,10):
                    self.sliders[numberOfBand].setDisabled(True)
                    self.sliders[numberOfBand].setValue(50)
<<<<<<< HEAD
=======
<<<<<<< HEAD
                self.WindowMode.setEnabled(True)
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
                self.slidersEnable=False
                self.OnOff.setText("ON")

    def edittingSliderValue(self,numberOfBand): 
        Gains[numberOfBand] = self.sliders[numberOfBand].value()/50

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
    def ApplyEqualizer(self):
        windowMode=Win_Fn[self.WindowMode.currentIndex()]
        self.FFTdata=WinFn(windowMode,self.freqs,Bands,Gains,self.FFTdata)
        self.UpdateMainData()
        
        
<<<<<<< HEAD
=======
>>>>>>> 71640f8... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6

        
def main():
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

<<<<<<< HEAD
=======
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
<<<<<<< HEAD
>>>>>>> ecea9d24070069505abe79de933e20b8b917f113
=======
>>>>>>> bc6ab04fc484c6229c2a55bbcecb90bfb2b0e707
=======
<<<<<<< HEAD
>>>>>>> ef09d7a... PopUp Functions
>>>>>>> b8a63c7... PopUp Functions
=======
>>>>>>> 71640f8... Update
>>>>>>> e17ad2f... Update
>>>>>>> db22d41947c05507ef56f72bd45f69a74a8272a6
