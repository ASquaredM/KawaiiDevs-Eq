class Data:
    def __init__(self,TimeData=None,FFTData=None,freqs=None,SampleRate=None,FileName=None,FilePath=None):
        self.assignAll(TimeData,FFTData,freqs,SampleRate,FileName,FilePath)

    def assignAll(self,TimeData=None,FFTData=None,freqs=None,SampleRate=None,FileName=None,FilePath=None):
        self.TimeData= TimeData
        self.FFTData= FFTData
        self.freqs= freqs
        self.SampleRate= SampleRate
        self.FileName= FileName
        self.FilePath= FilePath
    
    

