from PyQt5 import QtCore, QtGui, QtWidgets
import PopUpWindow as UI
import sys
from GetDataFromFile import wavData
from WidgetClass import PlotWidget
import sounddevice as sd
class Ui_PopUpWindow(UI.Ui_MainWindow):
    def __init__(self,mainWindow, Data1,Data2):
        self.mainWindow= mainWindow
        super(Ui_PopUpWindow,self).setupUi(mainWindow)
        def closeEvent(Event):
            sd.stop()
            Event.accept()
        self.mainWindow.closeEvent = closeEvent
        print(Data1.isNone(),Data2.isNone())
        if (Data1.isNone() or Data2.isNone()) :
            self.mainWindow.close()
        
        CompareTimeData=Data1.TimeData-Data2.TimeData
        CompareFFTData=Data1.FFTData-Data2.FFTData
        CompareData=wavData(TimeData=CompareTimeData,FFTData=CompareFFTData,freqs=Data1.freqs,SampleRate=Data1.SampleRate,FileName='',FilePath='')

        

        self.Data=[Data1,Data2,CompareData]

        
        self.Widgets=[
            PlotWidget(self.Data1TimeWidget,self.Data1FFTWidget,self.Data1PlayButton,self.Data1StopButton),
            PlotWidget(self.Data2TimeWidget,self.Data2FFTWidget,self.Data2PlayButton,self.Data2StopButton),
            PlotWidget(self.CompareTimeWidget,self.CompareFFTWidget,self.ComparePlayButton,self.CompareStopButton)
        ]
        
        """for i in range(0,3):
            self.Widgets[i].setHidden(True)"""
        self.graphAll()


    def graphAll(self):
        for indexOfWidget in range(0,3):
            print("Hi")
            if self.Data[indexOfWidget].isNone() is False:
                """self.Widgets[indexOfWidget].setHidden(False)"""
                self.Widgets[indexOfWidget].Graph(self.Data[indexOfWidget])

    def clearWidget(self,indexOfWidget):
        self.Widgets[indexOfWidget].setHidden(True)

    def PlayWidget(self,indexOfWidget):
        if self.Data[indexOfWidget].isNone() is False:
            print("Hi")
            sd.stop()
            sd.play(self.Data[indexOfWidget].TimeData,self.Data[indexOfWidget].SampleRate)


