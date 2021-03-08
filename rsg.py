import random
import math

def generateSignal(harmonics_count,frequency,N):
    signal = [0] * N

    for i in range (harmonics_count):

        W = (frequency / harmonics_count) * (i+1)
        Amplitude = random.random()
        Phase = random.random()

        for t in range(N):
            signal[t] += (Amplitude * math.sin(W * t + Phase))

    return signal