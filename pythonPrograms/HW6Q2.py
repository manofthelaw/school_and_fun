#HW6Q2
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt

piano = np.loadtxt("piano.txt", float)
trumpet = np.loadtxt("trumpet.txt", float)

#array for each value of text file
tPiano = np.arange(len(piano))
tTrumpet = np.arange(len(trumpet))

#transform each waveform
pTransform = np.fft.rfft(piano)
tTransform = np.fft.rfft(trumpet)

fig, axs = plt.subplots(2)
axs[0].plot(tPiano, piano)
axs[1].plot(abs(pTransform))
plt.show()

fig, axs = plt.subplots(2)
axs[0].plot(tTrumpet, trumpet)
axs[1].plot(abs(tTransform))
plt.show()

#Part a) discussion
#The single note on the piano is compsed of less frequencies
#than the single note for the trumpet.

#Part b)
#The notes being played seem to be D.
#The frequency with the largest amplitude for the piano was at 1190
#looking at a chart I found, it's close to D6
#The frequency with the largest amplitude for the trumpet was at 2367
#the chart shows D7 for that frequency



for i in tPiano:

    if abs(pTransform[i]) == max(abs(pTransform)):
        print(tPiano[i])
        break

for i in tTrumpet:

    if abs(tTransform[i]) == max(abs(tTransform)):
        print(tTrumpet[i])
        break
