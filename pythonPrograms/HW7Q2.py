#HW7Q2
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

m = 9.109e-31
L = 1e-8
xInitial = L/2
sigma = 1e-10
k = 5e+10
h = 1e-18 #time step
N = 1000 #spatial slices
a = L/N
hbar = 1e-34
t=0

psi0 = np.empty(N, dtype = complex)



for i in range(N):
    x = (i+0)*a
    psi0[i] = np.exp(-(x - xInitial)**2/(2*sigma**2))*np.exp(1.0j*k*x)

#plt.plot(psi0)
#plt.show()

a1 = 1 + (h*1.0j * hbar)/(2*m*a**2)
a2 = -h * (1.0j*hbar)/(4*m*a**2)
A = np.zeros([N,N], dtype = complex)

for k in range(N):
    A[k,k] = a1
    if k != N-1:
        A[k,k+1] = a2
        A[k+1,k] = a2

v = np.empty(N, dtype = complex)

b1 = 1 - (h*1.0j * hbar)/(2*m*a**2)
b2 = h * (1.0j*hbar)/(4*m*a**2)


for time in range(1000):
    for i in range(1, N-1):
        v[i] = b1*psi0[i] + b2*(psi0[i+1] + psi0[i-1])
    v[0] = b1*psi0[0] + b2*psi0[1]
    v[N-1] = b1*psi0[N-1] + b2*psi0[N-2]
    
    psi = np.linalg.solve(A,v)
    probability =(psi * np.conj(psi))
    psi0 = psi
    t += h
    plt.plot(probability)
    plt.draw()
    plt.pause(0.00001)
