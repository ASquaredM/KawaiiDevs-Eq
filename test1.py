import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

#split freqs array into bands and return signal with bands
def equalizer_10band (f, fs, gain1=0, gain2=0, gain3=0, gain4=0, gain5=0, gain6=0, gain7=0, gain8=0, gain9=0, gain10=0):
    band = int (len(f)/10)
    band1 = f[0:band]*(gain1)
    band2 = f[band : band*2]*(gain2)
    band3 = f[band*2 : band*3]*(gain3)
    band4 = f[band*3 : band*4]*(gain4)
    band5 = f[band*4 : band*5]*(gain5)
    band6 = f[band*5 : band*6]*(gain6)
    band7 = f[band*6 : band*7]*(gain7)
    band8 = f[band*7 : band*8]*(gain8)
    band9 = f[band*8 : band*9]*(gain9)
    band10 = f[band*9 : band*10]*(gain10)
    signal = np.concatenate([band1,band2,band3,band4,band5,band6,band7,band8,band9,band10])
    return signal

#read data and sampling freq
samplerate, data = wav.read(r'C:\Users\ooo\Desktop\REPOGAMDA\clapping.wav')

#create time array
t  = np.arange(len(data))/samplerate 
#create freq array
f  = samplerate/len(data) * np.arange(len(data))
#computing fft of original signal
f_data = np.fft.fft(data)/len(data)
f_data=abs(f_data)
#appying equalizer and change gain
equalized= equalizer_10band(data, samplerate, 0,0,0,0,0,0,0,0,0,0)
t= t[0:len(equalized)]
data= data[0:len(equalized)]

#computing fft of filtered signal
Y = np.fft.fft(equalized)/len(data)
Y=abs(Y)

plt.figure(figsize=(10, 8))
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
plt.xlim([0,5000])
plt.plot(f[:len(data)//2],np.abs(Y[:len(data)//2]),'-b',label=r"Equalized magnitude(f)")
plt.xlabel('f [Hz]')
plt.xlim([0,5000])
plt.legend()
plt.tight_layout()
plt.grid()