import UI
from PyQt5 import QtWidgets, QtCore
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import sys
from GetDataFromFile import getDataFromAFile
import scipy
import scipy.fftpack as fftpk


class ApplicationWindow(UI.Ui_MainWindow):
    def __init__(self,mainWindow):
        super(ApplicationWindow,self).setupUi(mainWindow)
        
        self.data=None
        self.FileName=None
        
        self.Open_File.clicked.connect(self.getData)
        self.Open_File.clicked.connect(self.graph)

        
    def getData(self):
        #get the file and read it#
        filePath=QtWidgets.QFileDialog.getOpenFileName(None,  'load', "./","All Files *;;" "*.wav;;" " *.mp3;;" "*.snd")
        dataFromTheFile=getDataFromAFile(filePath)
        Output,self.FileName = dataFromTheFile if dataFromTheFile is not None  else  [None,self.FileName]
        if Output is None:
            pass
        else:
            self.SampleRate,self.data=Output
            print(self.FileName,self.SampleRate )
    
    def graph(self):
        if self.data is not None:
            #graph the wav file#
            plot=self.data[:,1]
            FFT=abs(scipy.fft(self.data[:,1]))
            freqs =fftpk.fftfreq(len(FFT),(1.0/self.SampleRate))
            self.widget.plotItem.plot(freqs[range(len(FFT)//2)],FFT[range(len(FFT)//2)])
            self.widget.plotItem.plot(plot)
        
def main():
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ui=ApplicationWindow(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

