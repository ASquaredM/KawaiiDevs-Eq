class PlotWidget:
    def __init__(self,TimeWidget,FFTWidget):
        self.TimeWidget= TimeWidget
        self.FFTWidget= FFTWidget
    def Graph(self,Data):
        if Data.isNone() is False:
            print(Data.FFTData)
            self.TimeWidget.plotItem.clear()
            self.TimeWidget.plotItem.plot(Data.TimeData)
            self.FFTWidget.plotItem.clear()
            self.FFTWidget.plotItem.plot(Data.freqs[range(len(Data.FFTData)//2)],abs(Data.FFTData[range(len(Data.FFTData)//2)]))
    def setHidden(self,boolian):
        self.TimeWidget.setHidden(boolian)
        self.FFTWidget.setHidden(boolian)