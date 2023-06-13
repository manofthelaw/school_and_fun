#ODE Practice/Learning

import numpy as np
import matplotlib.pyplot as plt


def fxn(n,t):
    return -n/5*t

a,b,N = 0.0,10.0,1000
h = (b-a)/N



tPoints = np.linspace(a,b,N)
nPoints = [3000]

for t in tPoints[1:]:
    j1=h*fxn(nPoints[-1], t)
    j2=h*fxn(nPoints[-1]+0.5*j1, t+0.5*h)
    j3=h*fxn(nPoints[-1]+0.5*j2, t+0.5*h)
    j4=h*fxn(nPoints[-1]+j3, t+h)
    nPoints.append(nPoints[-1] + (1/6)*(j1+ 2*j2 + 2*j3 + j4))

plt.plot(tPoints,nPoints)
plt.xlabel("t")
plt.ylabel("N")
plt.grid(True)
plt.show()
 
