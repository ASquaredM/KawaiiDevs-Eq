import numpy as np
"""
freq = np.arange(20,5000)
Gains = [1,1,0,1,0,1,0,0,0,0]
Bands = np.array([[20,40],[40,80],[80,160]
                    ,[160,300],[300,600],[600,1200]
                    ,[1200,2400],[2400,5000],[5000,10000]
                    ,[10000,20000]])
data = np.arange(20,5000)
Win_Fn = np.array(['Rectangular','Hamming','Hanning'])
"""

def WinFn(Win_Fn,freq,Bands,Gains,data):
    stp = freq[3] - freq[2]
    lendata=len(data)
    positiveData=data[:lendata//2]
    halfOfRange=freq[:lendata//2]
    if Win_Fn == 'Rectangular':
        Win_data=Rec_Fn(positiveData,halfOfRange,Bands,Gains,stp)
    elif Win_Fn == 'Hamming':
        Win_data=Ham_Fn(positiveData,halfOfRange,Bands,Gains,stp)
    elif Win_Fn == 'Hanning':
        Win_data=Han_Fn(positiveData,halfOfRange,Bands,Gains,stp)
    positiveGainedData= Win_data
    zeros=np.zeros(lendata//2,dtype=complex)
    positiveDataFinal=np.concatenate([positiveGainedData,zeros])
    FlippedDate=np.flip(positiveGainedData)
    negativeDataFinal=np.concatenate([zeros,FlippedDate])
    Win_data=positiveDataFinal+negativeDataFinal

    return Win_data

def indxl(low,stp):
    indx = int(low//stp)
    return indx

  def indxh(high,stp):
    indx = int(high//stp)
    return indx

def Rec_Fn(data,freq,Bands,Gains,stp):
    len_freq = len(freq)
    Win_data = np.zeros(len_freq,dtype=complex)
    itr_outer = 0
    while itr_outer < 9:
        low = indxl(Bands[itr_outer][0],stp)
        high = indxh(Bands[itr_outer][1],stp)
        BW = high - low
        Shaper_Arr_Size = len_freq - high
        if Shaper_Arr_Size > 0 :
            Shaper_Arr = np.zeros((Shaper_Arr_Size),dtype=complex)
            Win_Fn_Arr = np.concatenate((np.zeros((low),dtype=complex),np.ones((BW),dtype=complex),Shaper_Arr),axis=0)
        else:
            BW = len_freq - low
            Win_Fn_Arr = np.concatenate((np.zeros((low),dtype=complex),np.ones((BW),dtype=complex)),axis=0)
        Win_data += (Win_Fn_Arr*data*Gains[itr_outer])
        itr_outer += 1
    return Win_data


def Ham_Fn(data,freq,Bands,Gains,stp):
    len_freq = len(freq)
    Win_data = np.zeros(len_freq,dtype=complex)
    itr_outer = 0
    out_data = np.zeros(0,dtype=complex)
    while itr_outer < 9:
        low = indxl(Bands[itr_outer][0],stp)
        high = indxh(Bands[itr_outer][1],stp)
        Hamm_Arr_Size = 2 * (high - low)
        Offset = abs(int((low - ((0.25) * Hamm_Arr_Size))))
        Shaper_Arr = np.zeros(0,dtype=complex)
        Shaper_Arr_Size = len_freq - Hamm_Arr_Size - Offset
        if Shaper_Arr_Size > 0 :
            Shaper_Arr = np.zeros(Shaper_Arr_Size,dtype=complex)
            Hamm_Fn_Arr = np.array(np.concatenate((np.zeros(Offset,dtype=complex),np.hamming(Hamm_Arr_Size),Shaper_Arr),axis=0),dtype=complex)
        else :
            Hamm_Arr_Size = len_freq - Offset
            Hamm_Fn_Arr = np.array(np.concatenate((np.zeros(Offset),np.hamming(Hamm_Arr_Size)),axis=0),dtype=complex)
        Win_data += data*Hamm_Fn_Arr[0:(len_freq)]*Gains[itr_outer]
        itr_outer += 1   
    return Win_data

def Han_Fn(data,freq,Bands,Gains,stp):
    len_freq = len(freq)
    Win_data = np.zeros(len_freq,dtype=complex)
    itr_outer = 0
    while itr_outer < 9:
        low = indxl(Bands[itr_outer][0],stp)
        high = indxh(Bands[itr_outer][1],stp)
        Hann_Arr_Size = 2 * (high - low)
        Offset = abs(int((low - ((0.25) * Hann_Arr_Size))))
        Shaper_Arr = np.zeros(0,dtype=complex)
        Shaper_Arr_Size = len_freq - Hann_Arr_Size - Offset
        if Shaper_Arr_Size > 0 :
            Shaper_Arr = np.zeros(Shaper_Arr_Size,dtype=complex)
            Hann_Fn_Arr = np.array(np.concatenate((np.zeros(Offset,dtype=complex),np.hanning(Hann_Arr_Size),Shaper_Arr),axis=0),dtype=complex)
        else :
            Hann_Arr_Size = len_freq - Offset
            Hann_Fn_Arr = np.array(np.concatenate((np.zeros(Offset),np.hanning(Hann_Arr_Size)),axis=0),dtype=complex)
        Win_data += data*Hann_Fn_Arr[0:(len_freq)]*Gains[itr_outer]
        itr_outer += 1   
    return Win_data



"""
Bass:
Deep Bass 20-40 Hz
Low Bass 40-80 Hz
Mid Bass 80-160 Hz
Upper Bass 160-300 Hz

Midrange:
Lower Midrange 300-600 Hz
Middle Midrange 600-1.2K Hz
Upper Midrange 1.2K-2.4K Hz
Presence Range 2.4K-5K Hz

High End:
High End 5K-10K Hz
Extremely High End 10K-20K Hz
"""