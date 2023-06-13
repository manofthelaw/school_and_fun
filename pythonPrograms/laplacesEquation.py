#LAPLACE'S EQUATION

from pylab import *
import numpy as np

# Constants
M = 50  #Grid squares on a side
V = 1.0  #Voltage at top wall
a=0.1
target = 1e-6

#Create arrays to hold the potential values
phi = zeros([M+1,M+1], float)
phi[0,:] = V
phiPrime = empty([M+1, M+1],float)

#Main Loop
delta = 1.0
while delta > target:

    #Calculate new values of the potential
    for i in range(M+1):
        for j in range(M+1):
            if i == 0 or i == M or j==0 or j==M:
                phiPrime[i,j] = phi[i,j]
            else:
                phiPrime[i,j] = (phi[i+1, j] + phi[i-1,j] + phi[i,j+1]\
                                 +phi[i,j-1])/4
    #Calculate maximum difference from old values
    #print(max(abs(phi-phiPrime)))
    delta = np.max(abs(phi-phiPrime))
    #print(delta)

    #Swap the two arrays around
    phi, phiPrime = phiPrime, phi

#plot
imshow(phi)
gray()
show()
