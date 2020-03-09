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
<<<<<<< HEAD
    stp = freq[3] - freq[2]
=======
    print(freq)
    print(data)
>>>>>>> 41b33545e38247e23b0ed79c74f73cabb631796f
    lendata=len(data)
    positiveData=data[:lendata//2]
    halfOfRange=freq[:lendata//2]
    if Win_Fn == 'Rectangular':
<<<<<<< HEAD
        Win_data=Rec_Fn(positiveData,halfOfRange,Bands,Gains,stp)
    elif Win_Fn == 'Hamming':
        Win_data=Ham_Fn(positiveData,halfOfRange,Bands,Gains,stp)
    elif Win_Fn == 'Hanning':
        Win_data=Han_Fn(positiveData,halfOfRange,Bands,Gains,stp)
    positiveGainedData= Win_data
    zeros=np.zeros(lendata//2,dtype=complex)
=======
        Win_data=Rec_Fn(positiveData,halfOfRange,Bands,Gains)
    elif Win_Fn == 'Hamming':
        Win_data=Ham_Fn(positiveData,halfOfRange,Bands,Gains)
    elif Win_Fn == 'Hanning':
        Win_data=Han_Fn(positiveData,halfOfRange,Bands,Gains)
    print(Win_data)
    positiveGainedData=np.array(Win_data,dtype=complex)#[len(Win_data)]
    print(positiveData)
    zeros=np.zeros(lendata//2,dtype=complex) 
    print(zeros) 
    #positiveData2 = [zeros,positiveData]  
>>>>>>> 41b33545e38247e23b0ed79c74f73cabb631796f
    positiveDataFinal=np.concatenate([positiveGainedData,zeros])
    FlippedDate=np.flip(positiveGainedData)
    negativeDataFinal=np.concatenate([zeros,FlippedDate])
    Win_data=positiveDataFinal+negativeDataFinal
<<<<<<< HEAD
    return Win_data

def indxl(low,stp):
    indx = int(low//stp)
    return indx
<<<<<<< HEAD
=======

>>>>>>> d9a0b44... Minor Edit
def indxh(high,stp):
    indx = int(high//stp)
    return indx

=======
    print(len(Win_data))
    print(len(freq))
    freq = np.array( freq [0:len(freq)-1])
    return [Win_data,freq]
>>>>>>> 41b33545e38247e23b0ed79c74f73cabb631796f

def Rec_Fn(data,freq,Bands,Gains,stp):
    len_freq = len(freq)
    Win_data = np.zeros(len_freq,dtype=complex)
    itr_outer = 0
    while itr_outer < 9:
<<<<<<< HEAD
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
=======
        itr_inner = 0
        Win_Fn_Arr = np.zeros(len_freq,dtype=complex)
        while itr_inner < len_freq:
            if ((freq[itr_inner] >= Bands[itr_outer][0]) and (freq[itr_inner] <= Bands[itr_outer][1]) ) :
                Win_Fn_Arr[itr_inner] = 1
            else:
                Win_Fn_Arr[itr_inner] = 0
            itr_inner+=1
            
        Win_data += np.array(Win_Fn_Arr,dtype=complex)*np.array(data,dtype=complex)*Gains[itr_outer]
>>>>>>> 41b33545e38247e23b0ed79c74f73cabb631796f
        itr_outer += 1
    return Win_data


def Ham_Fn(data,freq,Bands,Gains,stp):
    len_freq = len(freq)
    Win_data = np.zeros(len_freq,dtype=complex)
    itr_outer = 0
    out_data = np.zeros(0,dtype=complex)
    while itr_outer < 9:
<<<<<<< HEAD
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
=======
        if (Bands[itr_outer][0] or Bands[itr_outer][1]) in freq:
            #print('Band',itr_outer,Gains[itr_outer])
            Hamm_Arr_Size = 2 * ((Bands[itr_outer][1]) - (Bands[itr_outer][0]))
            Offset = abs(int((Bands[itr_outer][0]) - ((0.25) * Hamm_Arr_Size)))
            Shaper_Arr = np.zeros(0,dtype=complex)
            Shaper_Arr_Size = len_freq - Hamm_Arr_Size - Offset
            #print(Hamm_Arr_Size)
            #print(Offset)
            #print(Shaper_Arr_Size)
            if Shaper_Arr_Size > 0 :
                Shaper_Arr = np.zeros(Shaper_Arr_Size,dtype=complex)
                Hamm_Fn_Arr = np.array(np.concatenate((np.zeros(Offset,dtype=complex),np.hamming(Hamm_Arr_Size),Shaper_Arr),axis=0),dtype=complex)
            else :
                Hamm_Fn_Arr = np.array(np.concatenate((np.zeros(Offset),np.hamming(Hamm_Arr_Size)),axis=0),dtype=complex)
            #print(len(Hamm_Fn_Arr))
            out_data = np.array(data,dtype=complex)*Hamm_Fn_Arr[0:(len_freq)]*Gains[itr_outer]
            #print(out_data[Bands[itr_outer][0]:Bands[itr_outer][1]+ 50])
        else :
            break
        Win_data += out_data
>>>>>>> 41b33545e38247e23b0ed79c74f73cabb631796f
        itr_outer += 1   
    return Win_data

def Han_Fn(data,freq,Bands,Gains,stp):
    len_freq = len(freq)
    Win_data = np.zeros(len_freq,dtype=complex)
    itr_outer = 0
    while itr_outer < 9:
<<<<<<< HEAD
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
=======
        if (Bands[itr_outer][0] and Bands[itr_outer][1]) in freq:
            #print('Band',itr_outer,Gains[itr_outer])
            Hann_Arr_Size = 2 * (Bands[itr_outer][1] - Bands[itr_outer][0])
            Offset = abs(int(Bands[itr_outer][0] - ((0.25) * Hann_Arr_Size)))
            Shaper_Arr = np.zeros(0,dtype=complex)
            Shaper_Arr_Size = len_freq - Hann_Arr_Size - Offset
            #print(Hunn_Arr_Size)
            #print(Offset)
            #print(Shaper_Arr_Size)
            if Shaper_Arr_Size > 0 :
                Shaper_Arr = np.zeros(Shaper_Arr_Size,dtype=complex)
                Hann_Fn_Arr = np.array(np.concatenate((np.zeros(Offset),np.hanning(Hann_Arr_Size),Shaper_Arr),axis=0),dtype=complex)
            else :
                Hann_Fn_Arr = np.array(np.concatenate((np.zeros(Offset),np.hanning(Hann_Arr_Size)),axis=0),dtype=complex)
            #print(len(Hunn_Fn_Arr))
            out_data = np.array(data,dtype=complex)*Hann_Fn_Arr*Gains[itr_outer]
            #print(out_data[Bands[itr_outer][0]:Bands[itr_outer][1]+ 50])
        else :
            break
        Win_data += out_data
        itr_outer += 1
        
>>>>>>> 41b33545e38247e23b0ed79c74f73cabb631796f
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