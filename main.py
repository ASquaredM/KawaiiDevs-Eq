import UI
from PyQt5 import QtWidgets, QtCore
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import sys
import scipy
import scipy.io as sio
import scipy.fftpack as fftpk
import sounddevice as sd
import cmath
import Colors
from PopUpWindowClass import Ui_PopUpWindow
from WinFns import WinFn as WF
from GetDataFromFile import getDataFromAFile, wavData
from WidgetClass import PlotWidget

#Init a gain for each band
Gains = np.ones(10, dtype=complex)

#Freq. Spectrum Division (Setting Bands)
Bands = np.array(
    ([[20, 2000], [2000, 4000], [4000, 6000], [6000, 8000], [8000, 10000],
      [10000, 12000], [12000, 14000], [14000, 16000], [16000, 18000],
      [18000, 20000]]),
    dtype=complex)

DataBox = np.array(
    ['Original Data', 'Main Data', 'Quick Save 1', "Quick Save 2"])

#Supported Window Functions
Win_Fn = np.array(['Rectangular', 'Hamming', 'Hanning'])

#Saving Modes#
SaveMode = np.array(["To A File", "Save1", "Save2"])


class ApplicationWindow(UI.Ui_MainWindow):
    def __init__(self, mainWindow):
        super(ApplicationWindow, self).setupUi(mainWindow)

        self.Widgets = [
            PlotWidget(self.OpenedDataTimeWidget, self.OpenedDataFFTWidget,
                       self.OpenedDataPlayButton, self.OpenedDataStopButton),
            PlotWidget(self.MainDataTimeWidget, self.MainDataFFTWidget,
                       self.MainDataPlayButton, self.MainDataStopButton),
            PlotWidget(self.SavedData1TimeWidget, self.SavedData1FFTWidget,
                       self.SavedData1PlayButton, self.SavedData1StopButton),
            PlotWidget(self.SavedData2TimeWidget, self.SavedData2FFTWidget,
                       self.SavedData2PlayButton, self.SavedData2StopButton),
            PlotWidget(self.EqualizerDataTimeWidget,
                       self.EqualizerDataFFTWidget)
        ]
        self.OpenedData = wavData()
        self.MainData = wavData()
        self.SavedData1 = wavData()
        self.SavedData2 = wavData()

        self.Data = [
            self.OpenedData, self.MainData, self.SavedData1, self.SavedData2
        ]

        self.VariableInitialization()
        self.ButtonInitialization()
        self.sliderInitialization()

    def VariableInitialization(self):
        self.slidersEnable = False
        self.PopUpMenuIsON = False
        self.OpenedAFileEnable = False

    def ButtonInitialization(self):
        self.OpenFileButton.clicked.connect(self.OpenFile)
        self.OpenFileButton.clicked.connect(self.graphMainData)
        self.SaveButton.clicked.connect(self.saveSoundFile)
        self.ResetButton.clicked.connect(self.ResetMainData)
        self.CompareToButton.clicked.connect(self.OpenPopUpWindow)

    def OpenFile(self):
        #to stop playing the old music#
        sd.stop()
        #Get the Data from the File#
        filePath = QtWidgets.QFileDialog.getOpenFileName(
            None, 'load', "./", "All Files *;;"
            "*.wav;;")
        self.MainData = getDataFromAFile(filePath) if getDataFromAFile(
            filePath) is not None else self.MainData
        self.MainData.print()
        self.OpenedData.CopyFrom(self.MainData)
        self.Widgets[0].Graph(self.OpenedData)
        self.updateData()

    def updatePreEqualizerData(self):
        self.MainData.CopyFrom(self.OpenedData)
        self.updateData()

    def graphMainData(self):
        self.Widgets[1].Graph(self.MainData)
        self.Widgets[4].Graph(self.MainData)

    def updateData(self):
        self.Data = [
            self.OpenedData, self.MainData, self.SavedData1, self.SavedData2
        ]

    def ResetMainData(self):
        for numberOfBand in range(0, 10):
            self.sliders[numberOfBand].setRange(0, 100)
            self.sliders[numberOfBand].setValue(50)
        self.MainData.CopyFrom(self.OpenedData)
        self.updateData()

    def saveSoundFile(self):
        indexOfSaveModes = self.SaveMode.currentIndex()
        if SaveMode[indexOfSaveModes] == "To A File":
            name = QtGui.QFileDialog.getSaveFileName(
                None, 'Save File', self.MainData.FilePath + ".wav")[0]
            sio.wavfile.write(name, self.MainData.SampleRate,
                              self.MainData.TimeData)
        if SaveMode[indexOfSaveModes] == "Save1":
            self.SavedData1.CopyFrom(self.MainData)
            self.Widgets[2].Graph(self.SavedData1)
            self.updateData()
        if SaveMode[indexOfSaveModes] == "Save2":
            self.SavedData2.CopyFrom(self.MainData)
            self.Widgets[2].Graph(self.SavedData1)
            self.updateData()

    def OpenPopUpWindow(self):
        print("Opening a new popup window...")
        indexOfData1 = self.Data1ComboBox.currentIndex()
        indexOfData2 = self.Data2ComboBox.currentIndex()
        print(self.Data[indexOfData2].isNone(),
              self.Data[indexOfData1].isNone())
        if self.Data[indexOfData1].isNone(
        ) is False and self.Data[indexOfData2].isNone() is False:
            self.mainWindow = QtWidgets.QMainWindow()
            self.PopUp = Ui_PopUpWindow(self.mainWindow,
                                        self.Data[indexOfData1],
                                        self.Data[indexOfData2])
            self.mainWindow.show()

    def sliderInitialization(self):
        self.sliders = [
            self.Band1Slider, self.Band2Slider, self.Band3Slider,
            self.Band4Slider, self.Band5Slider, self.Band6Slider,
            self.Band7Slider, self.Band8Slider, self.Band9Slider,
            self.Band10Slider
        ]

        self.sliders[0].valueChanged.connect(
            lambda: self.edittingSliderValue(0))
        self.sliders[1].valueChanged.connect(
            lambda: self.edittingSliderValue(1))
        self.sliders[2].valueChanged.connect(
            lambda: self.edittingSliderValue(2))
        self.sliders[3].valueChanged.connect(
            lambda: self.edittingSliderValue(3))
        self.sliders[4].valueChanged.connect(
            lambda: self.edittingSliderValue(4))
        self.sliders[5].valueChanged.connect(
            lambda: self.edittingSliderValue(5))
        self.sliders[6].valueChanged.connect(
            lambda: self.edittingSliderValue(6))
        self.sliders[7].valueChanged.connect(
            lambda: self.edittingSliderValue(7))
        self.sliders[8].valueChanged.connect(
            lambda: self.edittingSliderValue(8))
        self.sliders[9].valueChanged.connect(
            lambda: self.edittingSliderValue(9))
        """self.sliders[0].valueChanged.connect(self.ApplyEqualizer)
        self.sliders[1].valueChanged.connect(self.ApplyEqualizer)
        self.sliders[2].valueChanged.connect(self.ApplyEqualizer)
        self.sliders[3].valueChanged.connect(self.ApplyEqualizer)
        self.sliders[4].valueChanged.connect(self.ApplyEqualizer)
        self.sliders[5].valueChanged.connect(self.ApplyEqualizer)
        self.sliders[6].valueChanged.connect(self.ApplyEqualizer)
        self.sliders[7].valueChanged.connect(self.ApplyEqualizer)
        self.sliders[8].valueChanged.connect(self.ApplyEqualizer)
        self.sliders[9].valueChanged.connect(self.ApplyEqualizer)"""

        self.ApplyEqualizerButton.clicked.connect(self.ApplyEqualizer)

        for numberOfBand in range(0, 10):
            self.sliders[numberOfBand].setRange(0, 100)
            self.sliders[numberOfBand].setValue(50)
            #self.sliders[numberOfBand].valueChanged.connect(lambda :self.edittingSliderValue(numberOfBand))

    def edittingSliderValue(self, numberOfBand):
        Gains[numberOfBand] = self.sliders[numberOfBand].value() / 50

    def ApplyEqualizer(self):
        sd.stop()
        windowMode = Win_Fn[self.WindowMode.currentIndex()]
        self.updatePreEqualizerData()
        newFFTdata = WF(windowMode, self.MainData.freqs, Bands, Gains,
                        self.MainData.FFTData)
        newTimeData = np.real(fftpk.ifft(newFFTdata))
        self.MainData.assignAll(FFTData=newFFTdata, TimeData=newTimeData)
        self.graphMainData()
        self.updateData()


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
