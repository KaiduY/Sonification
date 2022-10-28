import numpy as np
import matplotlib.pyplot as plt
from data import exemple


smrate, data = exemple()
plt.figure(1)
plt.title('Waveform')
plt.plot(data)
plt.show()
