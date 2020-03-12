import numpy as np

def WinFn(Win_Fn,freq,Bands,Gains,data):
<<<<<<< HEAD
    stp = freq[3] - freq[2]
<<<<<<< HEAD
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
=======

    if Win_Fn == 'Rectangular':
        Win_data=Rec_Fn(data,freq,Bands,Gains,stp)
>>>>>>> 3e70331... Fina Edits Insha'allah
    elif Win_Fn == 'Hamming':
        Win_data=Ham_Fn(data,freq,Bands,Gains,stp)
    elif Win_Fn == 'Hanning':
<<<<<<< HEAD
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
=======
        Win_data=Han_Fn(data,freq,Bands,Gains,stp)

>>>>>>> 3e70331... Fina Edits Insha'allah
    return Win_data

def indxl(low,stp,len_freq):
    indx = int(low//stp)
<<<<<<< HEAD
    return indx
<<<<<<< HEAD
=======

>>>>>>> d9a0b44... Minor Edit
def indxh(high,stp):
=======
    if indx < len_freq:
        return indx
    if indx > len_freq:
        return len_freq

def indxh(high,stp,len_freq):
>>>>>>> 97feae1... Window Function Fix Fix
    indx = int(high//stp)
    if indx < len_freq:
        return indx
    if indx > len_freq:
        return len_freq

=======
    print(len(Win_data))
    print(len(freq))
    freq = np.array( freq [0:len(freq)-1])
    return [Win_data,freq]
>>>>>>> 41b33545e38247e23b0ed79c74f73cabb631796f

def Rec_Fn(data,freq,Bands,Gains,stp):
    len_freq = int(len(freq) / 2)
    Win = np.zeros(0,dtype=complex)
    Win_data = np.zeros(len(freq),dtype=complex)
    itr_outer = 0
<<<<<<< HEAD
    while itr_outer < 9:
<<<<<<< HEAD
=======
    while itr_outer < 10:
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4403068... Minor Edits
        low = indxl(Bands[itr_outer][0],stp)
        high = indxh(Bands[itr_outer][1],stp)
=======
        low = indxl(Bands[itr_outer][0],stp,len_freq)
        high = indxh(Bands[itr_outer][1],stp,len_freq)
>>>>>>> 97feae1... Window Function Fix Fix
=======
        low = indxl(Bands[itr_outer][0],stp,len_freq) -1
        high = indxh(Bands[itr_outer][1],stp,len_freq) -1
>>>>>>> 3e70331... Fina Edits Insha'allah
        BW = high - low
        Shaper_Arr_Size = 2*(len_freq - high)
        if Shaper_Arr_Size > 0 :
            Shaper_Arr = np.zeros((Shaper_Arr_Size),dtype=complex)
            Win = np.multiply(np.ones(BW),Gains[itr_outer])
            Win_Fn_Arr = np.concatenate((np.zeros((low),dtype=complex),Win,Shaper_Arr,Win,np.zeros((low),dtype=complex)),axis=0)
        else:
            BW = len_freq - low
<<<<<<< HEAD
            #print('BW =' , BW)
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
<<<<<<< HEAD
>>>>>>> 41b33545e38247e23b0ed79c74f73cabb631796f
=======
<<<<<<< HEAD
>>>>>>> 0a4ab1edfc726b41f3687846c427a72ce38badb0
=======
<<<<<<< HEAD
>>>>>>> 0a738d6493cb4c2402a85edda9ffd2d16b032a7b
=======
<<<<<<< HEAD
>>>>>>> 82437c3dd0af84e062f7fefee34c5156a5a14161
=======
>>>>>>> dc7530858ef3acd56361880ba1847226e24b2fcc
=======
            Win = np.multiply(np.ones(BW),Gains[itr_outer])
            Win_Fn_Arr = np.concatenate((np.zeros((low),dtype=complex),Win,Win,np.zeros((low),dtype=complex)),axis=0)
        Win_data += Win_Fn_Arr*data
>>>>>>> 3e70331... Fina Edits Insha'allah
>>>>>>> 3cfda49... Fina Edits Insha'allah
>>>>>>> f143961... Fina Edits Insha'allah
>>>>>>> 377f2fe... Fina Edits Insha'allah
>>>>>>> 3af36a0... Fina Edits Insha'allah
        itr_outer += 1
    return Win_data

def Ham_Fn(data,freq,Bands,Gains,stp):
    len_freq = len(freq) / 2
    Win_data = np.zeros(len(freq),dtype=complex)
    itr_outer = 0
<<<<<<< HEAD
    out_data = np.zeros(0,dtype=complex)
    while itr_outer < 9:
<<<<<<< HEAD
=======
    while itr_outer < 10:
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4403068... Minor Edits
        low = indxl(Bands[itr_outer][0],stp)
        high = indxh(Bands[itr_outer][1],stp)
=======
        low = indxl(Bands[itr_outer][0],stp,len_freq)
        high = indxh(Bands[itr_outer][1],stp,len_freq)
>>>>>>> 97feae1... Window Function Fix Fix
        Hamm_Arr_Size = 2 * (high - low)
=======
        low = indxl(Bands[itr_outer][0],stp,len_freq) -1
        high = indxh(Bands[itr_outer][1],stp,len_freq) -1
<<<<<<< HEAD
        Hamm_Arr_Size = (high - low)
>>>>>>> 3e70331... Fina Edits Insha'allah
=======
        Hamm_Arr_Size = int(2*(high - low))
>>>>>>> c60ef45... Final Commit
        Offset = abs(int((low - ((0.25) * Hamm_Arr_Size))))
        Shaper_Arr = np.zeros(0,dtype=complex)
        Shaper_Arr_Size = int(2*(len_freq - Hamm_Arr_Size - Offset))
        Win = np.multiply(np.hamming(Hamm_Arr_Size),Gains[itr_outer])
        if Shaper_Arr_Size > 0 :
            Shaper_Arr = np.zeros(Shaper_Arr_Size,dtype=complex)
            Hamm_Fn_Arr = np.concatenate((np.zeros(Offset,dtype=complex),Win,Shaper_Arr,Win,np.zeros(Offset,dtype=complex)),axis=0)
        else :
<<<<<<< HEAD
<<<<<<< HEAD
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
<<<<<<< HEAD
>>>>>>> 41b33545e38247e23b0ed79c74f73cabb631796f
=======
<<<<<<< HEAD
>>>>>>> 0a4ab1edfc726b41f3687846c427a72ce38badb0
=======
<<<<<<< HEAD
>>>>>>> 0a738d6493cb4c2402a85edda9ffd2d16b032a7b
=======
<<<<<<< HEAD
>>>>>>> 82437c3dd0af84e062f7fefee34c5156a5a14161
=======
>>>>>>> dc7530858ef3acd56361880ba1847226e24b2fcc
=======
            Shaper_indx = len_freq-Offset -1
            Hamm_Fn_Arr = np.array(np.concatenate((np.zeros(Offset),Win[:Shaper_indx],np.flip(Win[:Shaper_indx],np.zeros(Offset))),axis=0),dtype=complex)
=======
            Shaper_indx = int(len_freq - Offset)
            Hamm_Fn_Arr = np.concatenate((np.zeros(Offset),Win[:Shaper_indx],np.flip(Win[:Shaper_indx]),np.zeros(Offset)),axis=0)
>>>>>>> c60ef45... Final Commit
        Win_data += data*Hamm_Fn_Arr
>>>>>>> 3e70331... Fina Edits Insha'allah
>>>>>>> 3cfda49... Fina Edits Insha'allah
>>>>>>> f143961... Fina Edits Insha'allah
>>>>>>> 377f2fe... Fina Edits Insha'allah
>>>>>>> 3af36a0... Fina Edits Insha'allah
        itr_outer += 1   
    return Win_data

def Han_Fn(data,freq,Bands,Gains,stp):
    len_freq = len(freq) / 2
    Win_data = np.zeros(len(freq),dtype=complex)
    itr_outer = 0
<<<<<<< HEAD
    while itr_outer < 9:
<<<<<<< HEAD
=======
    while itr_outer < 10:
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4403068... Minor Edits
        low = indxl(Bands[itr_outer][0],stp)
        high = indxh(Bands[itr_outer][1],stp)
=======
        low = indxl(Bands[itr_outer][0],stp,len_freq)
        high = indxh(Bands[itr_outer][1],stp,len_freq)
>>>>>>> 97feae1... Window Function Fix Fix
        Hann_Arr_Size = 2 * (high - low)
=======
        low = indxl(Bands[itr_outer][0],stp,len_freq) -1
        high = indxh(Bands[itr_outer][1],stp,len_freq) -1
<<<<<<< HEAD
        Hann_Arr_Size = (high - low)
>>>>>>> 3e70331... Fina Edits Insha'allah
=======
        Hann_Arr_Size = int(2*(high - low))
>>>>>>> c60ef45... Final Commit
        Offset = abs(int((low - ((0.25) * Hann_Arr_Size))))
        Shaper_Arr = np.zeros(0,dtype=complex)
        Shaper_Arr_Size = int(2*(len_freq - Hann_Arr_Size - Offset))
        Win = np.multiply(np.hanning(Hann_Arr_Size),Gains[itr_outer])
        if Shaper_Arr_Size > 0 :
            Shaper_Arr = np.zeros(Shaper_Arr_Size,dtype=complex)
            Hann_Fn_Arr = np.concatenate((np.zeros(Offset,dtype=complex),Win,Shaper_Arr,Win,np.zeros(Offset,dtype=complex)),axis=0)
        else :
            Shaper_indx = int(len_freq-Offset)
            Hann_Fn_Arr = np.concatenate((np.zeros(Offset),Win[:Shaper_indx],np.flip(Win[:Shaper_indx]),np.zeros(Offset)),axis=0)
        Win_data += data*Hann_Fn_Arr
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