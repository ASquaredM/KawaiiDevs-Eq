import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.signal import butter, lfilter

#create bandpass
def butter_bandpass(lowcut, highcut, fs, order=5):
    freqmx = 0.5 * fs
    low = lowcut / freqmx
    high = highcut / freqmx
    #butter returns Numerator (b) and denominator (a) polynomials of the IIR filter
    b, a = butter(order, [low, high], btype='band')
    return b, a

#return bands that filtered
def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    filtered = lfilter(b,a, data)
    return filtered

#create bands depends on freqs in the wav file
def equalizer_10band (data, fs, gain1=0, gain2=0, gain3=0, gain4=0, gain5=0, gain6=0, gain7=0, gain8=0, gain9=0, gain10=0):
    freqmax = fs/2
    freqmin = 0
    fb = (freqmax-freqmin)/11
    lowcut = 20 
    highcut = 20 +fb
    band1 = bandpass_filter(data, lowcut , highcut, fs, order=3)* (gain1/100)
    lowcut = 20 +fb
    highcut = 20 +2*fb
    band2 = bandpass_filter(data, lowcut, highcut, fs, order=3)*(gain2/100)
    lowcut = 20 +2*fb
    highcut = 20 +3*fb
    band3 = bandpass_filter(data, lowcut, highcut, fs, order=3)*(gain3/100)
    lowcut = 20 +3*fb
    highcut = 20 +4*fb
    band4 = bandpass_filter(data, lowcut, highcut, fs, order=3)* (gain4/100)
    lowcut = 20 +4*fb
    highcut = 20 +5*fb
    band5 = bandpass_filter(data, lowcut, highcut, fs, order=3)* (gain5/100)
    lowcut = 20 +5*fb
    highcut = 20 +6*fb
    band6 = bandpass_filter(data, lowcut, highcut, fs, order=3)* (gain6/100)
    lowcut = 20 +6*fb
    highcut = 20 +7*fb
    band7 = bandpass_filter(data, lowcut, highcut, fs, order=3)* (gain7/100)
    lowcut = 20 +7*fb
    highcut = 20 +8*fb
    band8 = bandpass_filter(data, lowcut, highcut, fs, order=3)* (gain8/100)
    lowcut = 20 +8*fb
    highcut = 20 +9*fb
    band9 = bandpass_filter(data, lowcut, highcut, fs, order=3)* (gain9/100)
    lowcut = 20 +9*fb
    highcut = 20+10*fb
    band10 = bandpass_filter(data, lowcut, highcut, fs, order=3)* (gain10/100)
    signal = band1 + band2 + band3 + band4 + band5 + band6 + band7 + band8 + band9 + band10
    return signal





samplerate, data = wav.read(r'C:\Users\ooo\ok.wav')
t  = np.arange(len(data))/samplerate 
#create freq array
f  = (samplerate/len(data)) * np.arange(len(data))

#computing fft of original signal
f_data = np.fft.fft(data)/len(data)
f_data=abs(f_data)

#appying equalizer and change gain
equalized= equalizer_10band(data, samplerate, 1000,1000,1000,1000,1000,1000,1000,1000,1000,1000)
#t= t[0:len(equalized)]
#data= data[0:len(equalized)]

#computing fft of filtered signal
Y = np.fft.fft(equalized)/len(data)
Y=abs(Y)

plt.figure(figsize=(30, 18))
plt.subplot(2,1,1)
plt.plot(t, equalized,'-b',label=r"Equalized amplitude(t)")
plt.xlabel('time[s]')
plt.subplot(2,1,1)
plt.plot(t, data,'-r',label=r"Original amplitude(t)")
plt.xlabel('time[s]')
plt.legend()
plt.grid()
plt.subplot(2,1,2)
plt.plot(f[:len(data)//2],np.abs(f_data[:len(data)//2]),'-r',label=r"Original magnitude(f)")
plt.xlabel('f [Hz]')
plt.xlim()
plt.plot(f[:len(data)//2],np.abs(Y[:len(data)//2]),'-b',label=r"Equalized magnitude(f)")
plt.xlabel('f [Hz]')
plt.xlim()
plt.legend()
plt.tight_layout()
plt.grid()

wave = wav.write("example5.wav", samplerate, equalized)




