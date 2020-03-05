import scipy.io as sio
import scipy.io.wavfile as siowav
import numpy as np
import soundfile as sf
import scipy.fftpack as fftpk
from PyQt5 import QtWidgets, QtCore

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
        data=wav(filePath)  
    else:
        return None
    """elif(datatype=="mp3"):
        data=mp3(filePath)  
    elif(datatype=="snd"):
        data=mp3(filePath)  """
    #print(data[1])
    return [data,filename,Path]

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

def wav(filename):
    #data= siowav.read(filename)
    data=sf.read(filename, dtype='float32')
    return data

def mp3(filename):
    pass
def snd(filename):
    pass


def getWavData():
    #get the file and read it#
    filePath=QtWidgets.QFileDialog.getOpenFileName(None,  'load', "./","All Files *;;" "*.wav;;" " *.mp3;;" "*.snd")
    dataFromTheFile=getDataFromAFile(filePath)
    if dataFromTheFile is not None:
        Output,FileName,Path = dataFromTheFile
        nChannelData,SampleRate=Output
        if  isinstance(nChannelData[0] ,np.ndarray):
            oneChannelData=nChannelData[:,0]
        else:
            oneChannelData=nChannelData
        FFTData=fftpk.fft(oneChannelData)
        freqs =fftpk.fftfreq(len(FFTData),(1.0/SampleRate))
        print(FFTData,freqs,SampleRate,FileName,Path)
        return FFTData,freqs,SampleRate,FileName,Path
    else:
        return None