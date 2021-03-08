import matplotlib.pyplot as plt 
import numpy as np 
import rsg
import dft

plt.style.use('bmh')

harmonics_count = 8
frequency = 1500
N = 1024

signals = rsg.generateSignal(harmonics_count,frequency,N)
ADFT = np.abs(dft.DFT(signals))

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
fig.subplots_adjust(hspace=0.5)
fig.set_size_inches(12,6)

ax1.plot(signals)
ax1.set_xlim(0, int(N/4))
ax1.set(xlabel='Time', ylabel='Signal(t)',
        title='Random generated signals')

ax2.plot(ADFT)
ax2.set_xlim(0, int(N/4))
ax2.set(xlabel='Time', ylabel='Freq (Hz)',
        title='Frequency spectrum')      

fig.savefig("plot.png")
plt.show()
