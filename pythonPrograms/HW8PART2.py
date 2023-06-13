#HW8PART2Q1
#Jeremy Lampley

import numpy as np
import random as rng
import matplotlib.pyplot as plt

N = 1000
T = 10.0

n = np.ones([N, 3], int)

eTotal = 3*N*np.pi**2/2

steps = 100000

ePlot = []

for k in range(steps):
    i = rng.randrange(N)
    j = rng.randrange(3)
    if rng.random()<0.5:
        dn = 1
        dE = (2*n[i,j] + 1)*np.pi**2/2
    else:
        dn = -1
        dE = (-2*n[i,j]+1)*np.pi**2/2

    if n[i,j]>1 or dn ==1:
        if rng.random()<np.exp(-dE/T):
            n[i,j] += dn
            eTotal += dE

    ePlot.append(eTotal)

plt.plot(ePlot)
plt.ylabel("Energy")
plt.show()
