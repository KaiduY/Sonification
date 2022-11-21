import numpy as np
import matplotlib.pyplot as plt
from data import example
from scipy.fft import fft, fftfreq, ifft
from scipy.signal import butter, find_peaks

smrate, data = example(n=1)

#Convert data to mono
mono = data.sum(axis = 1)
N = len(mono)

pk, _ = find_peaks(mono)

hpk = []
for pek in pk:
    hpk.append(mono[pek])

plt.figure(1)

peak = plt.subplot()
peak.plot(mono)
peak.plot(pk, hpk, 'r*')
plt.show()

#QUESTION WHICH PEAKS ARE ACTUALLY STARS? WE NEED MORE DATA BRUH ----> PUSH FASTER THE DATA GENERATION PART



#HOW TO DO A SPECTOGRAM/WATERFALL + FFT

#yf = fft(mono)
#xf = fftfreq(N, 1 / smrate)
#sig = ifft(yf)


#c = plt.subplot()
#Pxx, freqs, bins, im = c.specgram(sig, NFFT=2**10, Fs=smrate, noverlap=50)
#c.set_xlabel('Time')
#c.set_ylabel('Frequency')