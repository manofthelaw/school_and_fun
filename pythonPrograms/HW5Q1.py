#HW5Q1
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt


def fxn(n,t):
    return -n/5*t

a,b,N = 0.0,10.0,1000
h = (b-a)/N
n = 3000


tPoints = np.linspace(a,b,N)
nPoints = []

for t in tPoints:
    nPoints.append(n)
    j1=h*fxn(n, t)
    j2=h*fxn(n+0.5*j1, t+0.5*h)
    j3=h*fxn(n+0.5*j2, t+0.5*h)
    j4=h*fxn(n+j3, t+h)
    n += (j1+2*j2+2*j3+j4)/6
    

plt.plot(tPoints,nPoints)
plt.xlabel("t")
plt.ylabel("N")
plt.grid(True)
plt.show()
