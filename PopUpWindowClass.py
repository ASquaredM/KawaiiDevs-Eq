from PyQt5 import QtCore, QtGui, QtWidgets
import PopUpWindow as UI
import sys
from GetDataFromFile import getDataFromAFile, wavData
from WidgetClass import PlotWidget
import sounddevice as sd
class Ui_PopUpWindow(UI.Ui_MainWindow):
    def __init__(self,mainWindow, MainData,SavedData1,SavedData2):
        super(Ui_PopUpWindow,self).setupUi(mainWindow)
        
        self.Data=[MainData,SavedData1,SavedData2]
        
        self.Widgets=[
            PlotWidget(self.MainDataTimeWidget,self.MainDataFFTWidget),
            PlotWidget(self.SavedData1TimeWidget,self.SavedData1FFTWidget),
            PlotWidget(self.SavedData2TimeWidget,self.SavedData2FFTWidget)]
        
        for i in range(0,3):
            self.Widgets[i].setHidden(True)
        
        self.PlayWidget1Button.clicked.connect(lambda : self.PlayWidget(1))
        self.PlayWidget1Button.clicked.connect(lambda : self.PlayWidget(2))
        self.LoadFiletoWidget1Button.clicked.connect(lambda : self.LoadFile(1))
        self.LoadFiletoWidget2Button.clicked.connect(lambda : self.LoadFile(2))
        self.ClearWidget1Button.clicked.connect(lambda :self.clearWidget(1))
        self.ClearWidget2Button.clicked.connect(lambda :self.clearWidget(2))
        self.graphAll()

    def graphAll(self):
        for indexOfWidget in range(0,3):
            if self.Data[indexOfWidget] is not None:
                self.Widgets[indexOfWidget].setHidden(False)
                self.Widgets[indexOfWidget].Graph(self.Data[indexOfWidget])
        
    def LoadFile(self,indexOfWidget):
        filePath=QtWidgets.QFileDialog.getOpenFileName(None,  'load', "./","All Files *;;" "*.wav;;")
        data=getDataFromAFile(filePath)
        if data is not None:
            self.Data[indexOfWidget]=data
            self.Widgets[indexOfWidget].Graph(data)
            self.Widgets[indexOfWidget].setHidden(False)

    def clearWidget(self,indexOfWidget):
        self.Widgets[indexOfWidget].setHidden(True)

    def PlayWidget(self,indexOfWidget):
        sd.stop()
        sd.play(self.Data[indexOfWidget].TimeData,self.Data[indexOfWidget].SampleRate)



