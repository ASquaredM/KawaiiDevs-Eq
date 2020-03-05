import numpy as np

def WinFn(Win_Fn,freq,Bands,Gains,data):
    Win_data = np.zeros(len(freq))
    if Win_Fn == 'Rectangular':
        Win_data=Rec_Fn(data,freq,Bands,Gains)
    elif Win_Fn == 'Hamming':
        Win_data=Ham_Fn(data,freq,Bands,Gains)
    elif Win_Fn == 'Hanning':
        Win_data=Han_Fn(data,freq,Bands,Gains)

def Rec_Fn(data,freq,Bands,Gains):
    len_freq = len(freq)
    Win_data = np.zeros(0)
    itr_outer = 0
    while itr_outer < 9:
        itr_inner = 0
        Win_Fn_Arr = np.zeros(len_freq)
        while itr_inner < len_freq:
            if (freq[itr_inner] >= Bands[itr_outer][0] and freq[itr_inner] <= Bands[itr_outer][0] ):
                Win_Fn_Arr[itr_inner] = 1
            else:
                Win_Fn_Arr[itr_inner] = 0
            itr_inner+=1
            
        Win_data += Win_Fn_Arr*data*Gains[itr_outer]
        itr_outer += 1
    return Win_data


def Ham_Fn(data,freq,Bands,Gains):
    len_freq = len(freq)
    Win_data = np.zeros(0)
    itr_outer = 0
    while itr_outer < 9:
        itr_inner = 0
        if (Bands[itr_outer][0] or Bands[itr_outer][1]) in freq:
            #convert array to list for easy access to location of wanted element
            freq_list = list(freq)
            #get location of wanted element
            lowcut = freq_list.index(Bands[itr_outer][0])
            highcut = freq_list.index(Bands[itr_outer][1])
            Hamm_Arr_Size = 2 * (highcut - lowcut)
            Offset = abs(int(lowcut - ((0.25) * Hamm_Arr_Size)))
            Hamm_Fn_Arr = np.concatenate((np.zeros(Offset),np.hamming(Hamm_Arr_Size)
                            ,np.zeros(len_freq - Hamm_Arr_Size - Offset)),axis=0,out=None)
            #multiple the data from beginning "or lowcut" to our highcut in humming func and gain then connect the rest of data to have original array but modified in one band and 0 in other bands
            out_data = data*Hamm_Fn_Arr*Gains[itr_inner]
        Win_data += out_data
        itr_outer += 1
        
    return Win_data

def Han_Fn(data,freq,Bands,Gains):
    len_freq = len(freq)
    Win_data = np.zeros(0)
    itr_outer = 0
    while itr_outer < 9:
        itr_inner = 0
        if (Bands[itr_outer][0] or Bands[itr_outer][1]) in freq:
            #convert array to list for easy access to location of wanted element
            freq_list = list(freq)
            #get location of wanted element
            lowcut = freq_list.index(Bands[itr_outer][0])
            highcut = freq_list.index(Bands[itr_outer][1])
            Hunn_Arr_Size = 2 * (highcut - lowcut)
            Offset = abs(int(lowcut - ((0.25) * Hunn_Arr_Size)))
            Hunn_Fn_Arr = np.concatenate((np.zeros(Offset),np.hanning(Hunn_Arr_Size)
                            ,np.zeros(len_freq - Hunn_Arr_Size - Offset)),axis=0,out=None)
            #multiple the data from beginning "or lowcut" to our highcut in humming func and gain then connect the rest of data to have original array but modified in one band and 0 in other bands
            out_data = data*Hunn_Fn_Arr*Gains[itr_inner]
        Win_data += out_data
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