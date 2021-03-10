import matplotlib.pyplot as plt 
import rsg
import numpy as np
import fft

plt.style.use('bmh')

harmonics_count = 8
frequency = 1500
N = 1024

signals = rsg.generateSignal(harmonics_count,frequency,N)
AFFT = np.abs(fft.FFT(signals))

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
fig.subplots_adjust(hspace=0.5)
fig.set_size_inches(12,6)

ax1.plot(signals)
ax1.set_xlim(0, int(N/4))
ax1.set(xlabel='Time', ylabel='Signal(t)',
        title='Random generated signals')

ax2.plot(AFFT)
ax2.set_xlim(0, int(N/4))
ax2.set(xlabel='Time', ylabel='Freq (Hz)',
        title='Frequency spectrum(FFT)')      

fig.savefig("plot(fft).png")
plt.show()