import numpy as np


#band_1 gets data, freq arrays and gain
def bands_1(data,freq,gain1):
    #iterate on freq array and change freqs to be in between detected values
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >0 and freq <200 ):
            #can't write in data in this loop so we can make array from freq has ones or zeroes depending on freqs bands
              freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
    #make new data that have gain*freqs "freqs = [0 1 0 1 0 1 1 0 ]" so we can change gain of data and return new data
    data = freq*data*gain1
    
    return data



#just like band_1 
def bands_2(data,freq,gain2):
    
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >201 and freq <500 ):
                freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
        
    data = freq*data*gain2
    return data 




def bands_3(data,freq,gain3):
    
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >501 and freq <2000):
                freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
        
    data = freq*data*gain3
    return data




def bands_4(data,freq,gain4):
    
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >2001 and freq <3000 ):
                freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
        
    data = freq*data*gain4
    
    return data




def bands_5(data,freq,gain5):
    
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >3001 and freq <5000 ):
                freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
        
    data = freq*data*gain5
    return data



def bands_6(data,freq,gain6):
    
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >5001 and freq <7000 ):
               freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
        
    data = freq*data*gain6
    return data



def bands_7(data,freq,gain7):
     
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >7001 and freq <9000 ):
               freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
        
    data = freq*data*gain7
    return data



def bands_8(data,freq,gain8):
    
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >9001 and freq <12000 ):
                freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
        
    data = freq*data*gain8
    return data



def bands_9(data,freq,gain9):
     
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >12001 and freq <17000):
                freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
        
    data = freq*data*gain9
    return data



def bands_10(data,freq,gain10):
     
    with np.nditer(freq, op_flags=['readwrite']) as it:
        for freq in it:
            if (freq >17001 and freq <20000 ):
               freq[...] = freq/freq
            else:
                freq[...] = 0 * freq
        
    data = freq*data*gain10
    return data




#data is the result of ff
#freq is the result of fftpk.fftfreq(len(self.FFT),(1.0/self.SampleRate))
freq = np.arange(30)
gain1 = 1
gain2 = 1
gain3 = 1
gain4 = 1
gain5 = 1
gain6 = 1
gain7 = 1
gain8 = 1
gain9 = 1
gain10 = 1

data = np.arange(30 )
#signal will make summation for bands "band1= [5 0 5 0 0 5] and band_2=[0 10 0 10 10 0] so band_1 + band_2 = [5 10 5 10 10 5] "
signal = bands_1(data,freq,gain1) + bands_2(data,freq,gain2) + bands_3(data,freq,gain3) + bands_4(data,freq,gain4) + bands_5(data,freq,gain5) + bands_6(data,freq,gain6) + bands_7(data,freq,gain7) + bands_8(data,freq,gain8) + bands_9(data,freq,gain9) + bands_10(data,freq,gain10)
