import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy.signal import butter, lfilter

#create bandpass
def butter_bandpass(lowcut, highcut, fs, order=5):
    freqmx = fs/2
    low = lowcut / freqmx
    high = highcut / freqmx
    #butter returns Numerator (b) and denominator (a) polynomials of the IIR filter
    b, a = butter(order, [low, high], btype='band')
    return b, a

#return bands that filtered
def bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    filtered = 10*lfilter(b,a, data)
    return filtered

#create bands depends on freqs in the wav file
def equalizer_10band (data, fs, gain1=0, gain2=0, gain3=0, gain4=0, gain5=0, gain6=0, gain7=0, gain8=0, gain9=0, gain10=0):
    band1 = bandpass_filter(data, 20, 39, fs, order=2)*(gain1)
    band2 = bandpass_filter(data, 40, 79, fs, order=2)*(gain2)
    band3 = bandpass_filter(data, 80, 159, fs, order=2)*(gain3)
    band4 = bandpass_filter(data, 160, 299, fs, order=2)* (gain4)
    band5 = bandpass_filter(data, 300, 599, fs, order=2)* (gain5)
    band6 = bandpass_filter(data, 600, 1199, fs, order=2)*(gain6)
    band7 = bandpass_filter(data, 1200, 2399, fs, order=2)*(gain7)
    band8 = bandpass_filter(data, 2400, 4999, fs, order=2)* (gain8)
    band9 = bandpass_filter(data, 5000, 9999, fs, order=2)* (gain9)
    band10 = bandpass_filter(data, 10000, 20000, fs, order=2)*(gain10)
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
equalized= equalizer_10band(data, 44100 , 1,2,3,4,5,6,7,8,9,10)
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

wave = wav.write("example5.wav", int(samplerate), equalized)




