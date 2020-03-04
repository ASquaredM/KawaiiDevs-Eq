import numpy as np



def bands_1(data,freq,gain1):
  
    for i in freq:
            if (200 or 500) in freq:
                #convert array to list for easy access to location of wanted element
                freq = list(freq)
                #get location of wanted element
                highcut = freq.index(500)
                #multiple the data from beginning "or lowcut" to our highcut in humming func and gain then connect the rest of data to have original array but modified in one band and 0 in other bands
                data = np.concatenate(data[:highcut+2] *np.hanning(highcut +2)*gain1, 0*data[highcut+3:])
            else:
                break
    return data



#same as band_1
def bands_2(data,freq,gain2):
    
    for i in freq:
            if (200 or 500) in freq:
                freq = list(freq)
                lowcut = freq.index(200)
                highcut = freq.index(500)
                data = np.concatenate(0*data[:lowcut-3],data[lowcut-2:highcut+2] *np.hanning(highcut +2)*gain2,0* data[highcut+3:])
            else:
                break   
    return data



def bands_3(data,freq,gain3):
    
    for i in freq:
            if (501 or 2000) in freq:
                freq = list(freq)
                lowcut = freq.index(501)
                highcut = freq.index(2000)
                data = np.concatenate(0*data[:lowcut-3],data[lowcut-2:highcut+2] *np.hanning(highcut +2)*gain2,0* data[highcut+3:])
            else:
                break   
    return data



def bands_4(data,freq,gain4):
   
    for i in freq:
            if (2001 or 3000) in freq:
                freq = list(freq)
                lowcut = freq.index(2001)
                highcut = freq.index(3000)
                data = np.concatenate(0*data[:lowcut-3],data[lowcut-2:highcut+2] *np.hanning(highcut +2)*gain2, 0* data[highcut+3:])
            else:
                break
    return data



def bands_5(data,freq,gain5):
    freq = list(freq)
    lowcut = freq.index(3001)
    highcut = freq.index(5000)
    for i in freq:
            freq = list(freq)
            lowcut = freq.index(3001)
            highcut = freq.index(5000)
            if (3001 or 5000) in freq:
                data = np.concatenate(0*data[:lowcut-3],data[lowcut-2:highcut+2] *np.hanning(highcut +2)*gain2, 0*data[highcut+3:])
            else:
                break
    return data



def bands_6(data,freq,gain6):
    
    for i in freq:
            if (5001 or 7000) in freq:
                freq = list(freq)
                lowcut = freq.index(5001)
                highcut = freq.index(7000)
                data = np.concatenate(0*data[:lowcut-3],data[lowcut-2:highcut+2] *np.hanning(highcut +2)*gain2, 0*data[highcut+3:])
            else:
                break
    return data



def bands_7(data,freq,gain7):
   
    for i in freq:
            if (7001 or 9000) in freq:
                freq = list(freq)
                lowcut = freq.index(7001)
                highcut = freq.index(9000)
                data = np.concatenate(0*data[:lowcut-3],data[lowcut-2:highcut+2] *np.hanning(highcut +2)*gain2,0* data[highcut+3:])
            else:
                break
    return data



def bands_8(data,freq,gain8):
    
    for i in freq:
        if (9001 or 12000) in freq:
            freq = list(freq)
            lowcut = freq.index(9001)
            highcut = freq.index(12000)
            data = np.concatenate(0*data[:lowcut-3],data[lowcut-2:highcut+2] *np.hanning(highcut +2)*gain2, 0*data[highcut+3:])
        else:
            break
    return data



def bands_9(data,freq,gain9):
   
    for i in freq:
        if (12001 or 17000) in freq:
            freq = list(freq)
            lowcut = freq.index(12001)
            highcut = freq.index(17000)
            data = np.concatenate(0*data[:lowcut-3],data[lowcut-2:highcut+2] *np.hanning(highcut +2)*gain2, 0*data[highcut+3:])
        else:
            break    
    return data



def bands_10(data,freq,gain10):
   
    for i in freq:
            if (17001 or 20000) in freq:
                freq = list(freq)
                lowcut = freq.index(17001)
                highcut = freq.index(20000)
                data = np.concatenate(0*data[:lowcut-3],data[lowcut-2:highcut+2] *np.hanning(highcut +2)*gain2,0* data[highcut+3:])
            else:
                break
    return data



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
signal = bands_1(data,freq,gain1) + bands_2(data,freq,gain2) + bands_3(data,freq,gain3) + bands_4(data,freq,gain4) + bands_5(data,freq,gain5) + bands_6(data,freq,gain6) + bands_7(data,freq,gain7) + bands_8(data,freq,gain8) + bands_9(data,freq,gain9) + bands_10(data,freq,gain10)
