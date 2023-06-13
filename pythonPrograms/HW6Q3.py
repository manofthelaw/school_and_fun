#HW6Q3
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt

#Read in the data
dow1 = np.loadtxt("dow1.txt", float)


#array for each dow
tDow1 = np.arange(len(dow1))


#Calculate the coefficients
dow1Coeff = np.fft.rfft(dow1)
dow2Coeff = np.fft.rfft(dow1)


#Set all but first 10% to Zero
newDow1 = dow1Coeff
newDow1[int(0.1*len(dow1Coeff)):] = 0

#Set all but first 2% to Zero
newDow2 = dow2Coeff
newDow2[int(0.02*len(dow2Coeff)):] = 0

#Calculate inverse Fourier Transform of resulting array
newDow1Inv = np.fft.irfft(newDow1)
newDow2Inv = np.fft.irfft(newDow2)

#compare 10% removal
plt.plot(tDow1,dow1)
plt.plot(tDow1,newDow1Inv)
plt.show()
#This seems to smooth out the line for the original graph

#compare 2% removal
plt.plot(tDow1,dow1)
plt.plot(tDow1,newDow2Inv)
plt.show()
#This smooths it out even more, but seems less accurate
