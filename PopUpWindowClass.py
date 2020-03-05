from PyQt5 import QtCore, QtGui, QtWidgets
import PopUpWindow as UI
import sys
from GetDataFromFile import getWavData

class Ui_PopUpWindow(UI.Ui_MainWindow):
    def __init__(self,mainWindow, MainData,SavedData1,SavedData2):
        super(Ui_PopUpWindow,self).setupUi(mainWindow)
        self.Data=[MainData,SavedData1,SavedData2]
        self.Widgets=[self.MainDataWidget,self.SavedData1Widget,self.SavedData2Widget]
        self.MainData=MainData
        self.SavedData1=SavedData1
        self.SavedData2=SavedData2
        self.SavedData1Widget.setHidden(True)
        self.SavedData2Widget.setHidden(True)
        self.LoadFiletoWidget1Button.clicked.connect(lambda : self.LoadFile(1))
        self.LoadFiletoWidget2Button.clicked.connect(lambda : self.LoadFile(2))
        self.ClearWidget1Button.clicked.connect(lambda :self.clearWidget(1))
        self.ClearWidget1Button.clicked.connect(lambda :self.clearWidget(2))
        self.graphAll()

    def graphAll(self):
        if self.MainData is not None:
            self.graph(self.MainData,self.MainDataWidget)
            if self.SavedData1 is not None:
                self.LoadFiletoWidget1Button.setHidden(False)
                self.SavedData1Widget.setHidden(False)
                self.graph(self.SavedData1,self.SavedData1Widget)
            if self.SavedData2 is not None:
                self.LoadFiletoWidget2Button.setHidden(False)
                self.SavedData2Widget.setHidden(False)
                self.graph(self.SavedData2,self.SavedData2Widget)

    def LoadFile(self,indexOfWidget):
        data=getWavData()
        if data is not None:
            self.Data[indexOfWidget]=data()
            self.Widgets[indexOfWidget].plotItem.clear()
            self.graph(self.Data[indexOfWidget],self.Widgets[indexOfWidget])
            self.Widgets[indexOfWidget].setHidden(False)

    def clearWidget(self,indexOfWidget):
        self.Widgets[indexOfWidget].setHidden(True)

    def graph(self,data,Widget):
        FFTdata=data[0]
        freqs=data[1]
        Widget.plotItem.plot(freqs[range(len(FFTdata)//2)],abs(FFTdata[range(len(FFTdata)//2)]))

