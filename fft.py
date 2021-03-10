import math

def calcCoef(p, N):
    return (math.cos(2.0 * math.pi * p / N) + math.sin(2.0 * math.pi * p / N) * 1j)

def FFT(signals):

    N = len(signals)
    if N == 1: 
        return signals
    
    FFT_spec = [0] * N

    evens = FFT(signals[::2])
    odds = FFT(signals[1::2])

    length = N/2

    for p in range(int(length)):
        w = calcCoef(p, N)
        incalc = odds[p] * w

        FFT_spec[p] = evens[p] + incalc
        FFT_spec[p + int(length)] = evens[p] - incalc

    return FFT_spec






    


    