import numpy as np
import matplotlib.pyplot as plt
from data import example
from scipy.fft import fft, fftfreq, ifft
from scipy.signal import butter

smrate, data = example(n=1)

#Convert data to mono
mono = data.sum(axis = 1)
N = len(mono)
yf = fft(mono)
xf = fftfreq(N, 1 / smrate)

#print(yf)

cutoff = 10 * 1e3
#High pass filter
for i, sample in enumerate(yf):
    if abs(sample) < cutoff:
        #print(abs(sample))
        yf[i] = 0

sig = ifft(yf)

plt.figure(1)
c = plt.subplot()
Pxx, freqs, bins, im = c.specgram(sig, NFFT=2**10, Fs=smrate, noverlap=50)
c.set_xlabel('Time')
c.set_ylabel('Frequency')
plt.show()


#plt.figure(1)
#plt.title('Waveform')
#plt.plot(xf, np.abs(yf))
#plt.show()
