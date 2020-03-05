from PyQt5 import QtCore, QtGui, QtWidgets
import PopUpWindow as UI
import sys


class Ui_PopUpWindow(UI.Ui_MainWindow):
    def __init__(self,mainWindow, MainData,SavedData1,SavedData2):
        super(Ui_PopUpWindow,self).setupUi(mainWindow)
        self.MainData=MainData
        self.SavedData1=SavedData1
        self.SavedData2=SavedData2
        self.graphAll()

    def graphAll(self):
        if self.MainData is not None:
            FFTdata=self.MainData[0]
            freq=self.MainData[1]
            self.graph(FFTdata,freq,self.MainDataWidget)
            if self.MainData is not None:
                FFTdata=self.MainData[0]
                freq=self.MainData[1]
                self.graph(FFTdata,freq,self.SavedData1Widget)
            if self.MainData is not None:
                FFTdata=self.MainData[0]
                freq=self.MainData[1]
                self.graph(FFTdata,freq,self.SavedData2Widget)

    def graph(self,data,freqs,Widget):
        Widget.plotItem.plot(freqs[range(len(data)//2)],abs(data[range(len(data)//2)]))

def BuildPopUpWindow(MainData,SavedData1,SavedData2):
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    Ui_PopUpWindow(mainWindow,MainData,SavedData1,SavedData2)
    mainWindow.show()
    sys.exit(app.exec_())
    
#if __name__ == "__main__":
#    BuildPopUpWindow()
