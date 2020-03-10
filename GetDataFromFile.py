import scipy.io as sio
import scipy.io.wavfile as siowav
import numpy as np
import soundfile as sf
import scipy.fftpack as fftpk
from PyQt5 import QtWidgets, QtCore


class wavData:
    def __init__(self,TimeData=None,FFTData=None,freqs=None,SampleRate=None,FileName=None,FilePath=None):
        if TimeData is None and FFTData is None and freqs is None and SampleRate is None and FileName is None and FilePath is None:
            self.IsNone=True
            return
        self.assignAll(TimeData,FFTData,freqs,SampleRate,FileName,FilePath)
        self.IsNone=False

    def assignAll(self,TimeData=None,FFTData=None,freqs=None,SampleRate=None,FileName=None,FilePath=None):
        if TimeData is not None:
            self.TimeData= TimeData
        if FFTData is not None:
            self.FFTData= FFTData
        if freqs is not None:
            self.freqs= freqs
        if SampleRate is not None:
            self.SampleRate= SampleRate
        if FileName is not None:
            self.FileName= FileName
        if FilePath is not None:
            self.FilePath= FilePath
        self.IsNone=False


    def CopyFrom(self,OriginalData):
        self.assignAll(
        TimeData= OriginalData.TimeData,
        FFTData= OriginalData.FFTData,
        freqs= OriginalData.freqs,
        SampleRate= OriginalData.SampleRate,
        FileName=OriginalData.FileName,
        FilePath= OriginalData.FilePath)

    def print(self):
        print(self.TimeData,self.FFTData,self.freqs,self.SampleRate,self.FileName,self.FilePath)
    
    def isNone(self):
        return self.IsNone

def getDataFromAFile(filePath):
    filePath=filePath[0]
    data= None
    #getting the filename indexes in the filepath#
    BegOfTheName= filePath.rfind('/')+1 
    LastOfTheName= filePath.rfind('.')
    filename=filePath[BegOfTheName:LastOfTheName] 
    Path=filePath[:BegOfTheName]
    datatype = filePath[LastOfTheName+1:] #get the datatype from the filePath
    #making sure of the file type and read it#
    if(datatype=="txt" or datatype=="csv"):
        data=txt(filePath)
    elif(datatype=="mat"):
        data=mat(filePath)  
    elif(datatype=="wav"):
        data=wav(filePath,filename)  
    else:
        return None
    return data

def mat(filename):
    data=sio.loadmat(filename)
    for i in data:
        if '__' not in i and 'readme' not in i:
            np.savetxt(("./__pycache__/file.csv"),data[i],delimiter=',')
    data = np.loadtxt("./__pycache__/file.csv", delimiter=',')
    return data

def txt(filename):
    data = np.loadtxt(filename, delimiter=',')
    return data


def wav(filePath,FileName):
    dataFromTheFile=sf.read(filePath, dtype='float32')
    if dataFromTheFile is not None:
        nChannelData,SampleRate=dataFromTheFile
        if  isinstance(nChannelData[0] ,np.ndarray):
            oneChannelData=nChannelData[:,0]
        else:
            oneChannelData=nChannelData
        FFTData=fftpk.fft(oneChannelData)
        freqs =fftpk.fftfreq(len(FFTData),(1.0/SampleRate))
        Data=wavData(oneChannelData,FFTData,freqs,SampleRate,FileName,filePath)
        print(Data)
        return Data
    else:
        return None