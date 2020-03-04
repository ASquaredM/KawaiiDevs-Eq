import numpy as np



def bands_1(data,freq,gain1):
    #convert array to list for easy access to location of wanted element
    freq = list(freq)
    #get location of wanted element
    highcut = freq.index(200)
    #convert freq to array again "not essential"
    freq = np.array(freq)
    #multiple the data from beginning "or lowcut" to our highcut in humming func and gain then connect the rest of data to have original array but modified in one band
    data = np.concatenate(data[:highcut+2] *np.hamming(highcut +2)*gain1, data[highcut+3:])
    return data

#same as band_1
def bands_2(data,freq,gain2):
    freq = list(freq)
    lowcut = freq.index(200)
    highcut = freq.index(500)
    freq = np.array(freq)
    data = np.concatenate(data[:lowcut-3],data[lowcut-2:highcut+2] *np.hamming(highcut +2)*gain2, data[highcut+3:])
    return data

def bands_3(data,freq,gain3):
    freq = list(freq)
    lowcut = freq.index(501)
    highcut = freq.index(2000)
    freq = np.array(freq)
    data = np.concatenate(data[:lowcut-3],data[lowcut-2:highcut+2] *np.hamming(highcut +2)*gain2, data[highcut+3:])
    return data

def bands_4(data,freq,gain4):
    freq = list(freq)
    lowcut = freq.index(2001)
    highcut = freq.index(3000)
    freq = np.array(freq)
    data = np.concatenate(data[:lowcut-3],data[lowcut-2:highcut+2] *np.hamming(highcut +2)*gain2, data[highcut+3:])
    return data

def bands_5(data,freq,gain5):
    freq = list(freq)
    lowcut = freq.index(3001)
    highcut = freq.index(5000)
    freq = np.array(freq)
    data = np.concatenate(data[:lowcut-3],data[lowcut-2:highcut+2] *np.hamming(highcut +2)*gain2, data[highcut+3:])

    return data



def bands_6(data,freq,gain6):
    freq = list(freq)
    lowcut = freq.index(5001)
    highcut = freq.index(7000)
    freq = np.array(freq)
    data = np.concatenate(data[:lowcut-3],data[lowcut-2:highcut+2] *np.hamming(highcut +2)*gain2, data[highcut+3:])
    return data



def bands_7(data,freq,gain7):
    freq = list(freq)
    lowcut = freq.index(7001)
    highcut = freq.index(9000)
    freq = np.array(freq)
    data = np.concatenate(data[:lowcut-3],data[lowcut-2:highcut+2] *np.hamming(highcut +2)*gain2, data[highcut+3:])

    return data



def bands_8(data,freq,gain8):
    freq = list(freq)
    lowcut = freq.index(9001)
    highcut = freq.index(12000)
    freq = np.array(freq)
    data = np.concatenate(data[:lowcut-3],data[lowcut-2:highcut+2] *np.hamming(highcut +2)*gain2, data[highcut+3:])
    return data



def bands_9(data,freq,gain9):
    freq = list(freq)
    lowcut = freq.index(12001)
    highcut = freq.index(17000)
    freq = np.array(freq)
    data = np.concatenate(data[:lowcut-3],data[lowcut-2:highcut+2] *np.hamming(highcut +2)*gain2, data[highcut+3:])
    return data



def bands_10(data,freq,gain10):
    freq = list(freq)
    lowcut = freq.index(17000)
    highcut = freq.index(20000)
    freq = np.array(freq)
    data = np.concatenate(data[:lowcut-3],data[lowcut-2:highcut+2] *np.hamming(highcut +2)*gain2, data[highcut+3:])

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
