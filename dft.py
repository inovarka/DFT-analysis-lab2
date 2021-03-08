import math

def DFT(signals):

    L = len(signals)
    DFT = [0] * L

    for p in range(L):
        for k in range(L):
            DFT[p] += signals[k] * (math.cos(2.0 * math.pi * p * k / L) - math.sin(2.0 * math.pi * p * k / L) * 1j)
    
    return DFT