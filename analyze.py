import numpy as np
import matplotlib.pyplot as plt
from data import example
from scipy.fft import fft, fftfreq

smrate, data = example(n=1)

#Convert data to mono
mono = data.sum(axis = 1)
N = len(mono)
yf = fft(mono)
xf = fftfreq(N, 1 / smrate)

plt.figure(1)
plt.title('Waveform')
plt.plot(xf, np.abs(yf))
plt.show()
