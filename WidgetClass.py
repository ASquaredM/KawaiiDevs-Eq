from GetDataFromFile import wavData
import sounddevice as sd
class PlotWidget:
    def __init__(self,TimeWidget,FFTWidget,PlayButton=None,StopButton=None):
        self.playButton=PlayButton
        self.stopButton=StopButton
        self.TimeWidget= TimeWidget
        self.FFTWidget= FFTWidget
        self.Data=wavData()
        if PlayButton is not None and StopButton is not None and self.Data:
            self.playButton.clicked.connect(self.generateSound)
            self.stopButton.clicked.connect(self.stopSound)
    def Graph(self,Data):
        if Data.isNone() is False:
            self.Data.CopyFrom(Data)
            #print(Data.FFTData)
            self.TimeWidget.plotItem.clear()
            self.TimeWidget.plotItem.plot(Data.TimeData)
            self.FFTWidget.plotItem.clear()
            self.FFTWidget.plotItem.plot(Data.freqs[range((len(Data.FFTData)//2) -1)],abs(Data.FFTData[range((len(Data.FFTData)//2) -1)]))
    def setHidden(self,boolian):
        self.TimeWidget.setHidden(boolian)
        self.FFTWidget.setHidden(boolian)
        self.playButton.setHidden(boolian)
        self.stopButton.setHidden(boolian)
    def generateSound(self):
        sd.stop()
        sd.play(self.Data.TimeData,self.Data.SampleRate)  
    def stopSound(self):
        sd.stop()
    