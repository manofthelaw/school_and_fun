#HW6Q1
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt

dataPoints = 1000
timeStep = 1/dataPoints
freq = 50
N = int(dataPoints/freq)

tList = np.linspace(0, (N-1)*timeStep, N)
tSpaceSignal = 0.5*np.sin(2 * np.pi * freq *tList) +\
               0.6*np.sin(10*np.pi*freq*tList) + \
               0.3*np.sin(14*np.pi*freq*tList)

cfft = np.fft.rfft(tSpaceSignal)

plt.plot(tList, tSpaceSignal)
plt.show()

plt.plot(abs(cfft))
plt.show()
