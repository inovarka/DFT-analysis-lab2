import rsg
import fft
import numpy as np
from time import perf_counter

harmonics_count = 8
frequency = 1500


for i in range(2,13):
    N = 2**i
    signals = rsg.generateSignal(harmonics_count,frequency,N)

    t_start = perf_counter()
    fft.FFT(signals)
    t_end = perf_counter()
    time1 = t_end - t_start 

    t_start = perf_counter()
    np.fft.fft(signals)
    t_end = perf_counter()
    time2 = t_end - t_start

    print("N = 2^{0} ".format(i))
    print("time : {0}s (my fft)".format(time1))
    print("time : {0}s (numpy fft)\n".format(time2))
