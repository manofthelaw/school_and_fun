#HW7Q1
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt

#constants
l = 0.01 #length of material
D = 4.25e-6 #diffusivity
h = 1e-4 #time step
n = 100 #number of spaces
a = l/n #spacing
epsilon = h/1000

tLow = 0 
tMid = 20
tHigh = 50

t1 = 0.010
t2 = 0.1
t3 = 0.4
t4 = 10.0
t5 = 15.0
tEnd = t5 + epsilon

tI = np.empty(n+1, float)
tI[0] = tHigh
tI[n] = tLow
tI[1:n] = tMid

tF = np.empty(n+1, float)
tF[0] = tHigh
tF[n] = tLow

t = 0.0
c = h*D/(a*a)

while t < tEnd:

    
    tF[1:n] = tI[1:n] + c*(tI[2:n+1] + tI[0:n-1] - 2 * tI[1:n])
    tI, tF = tF, tI
    t += h
    

    #plots
    if abs(t-t1)<epsilon:
        plt.plot(tI)
    if abs(t-t2)<epsilon:
        plt.plot(tI)
    if abs(t-t3)<epsilon:
        plt.plot(tI)
    if abs(t-t4)<epsilon:
        plt.plot(tI)
    if abs(t-t5)<epsilon:
        plt.plot(tI)

plt.xlabel("x")
plt.ylabel("T")
plt.show()
