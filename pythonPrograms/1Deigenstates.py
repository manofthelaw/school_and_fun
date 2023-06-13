# Mr. P Solver Eigenstates of any 1D Potential in Python

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh_tridiagonal

#Define what N and dy are
N = 2000
dy = 1/N
y = np.linspace(0, 1, N+1)

#Define potential mL2V
def mL2V(y):
    return 1000*np.sin(20*y) * y**4 

d = 1/dy**2 + mL2V(y)[1: -1]
e = -1/(2*dy**2) * np.ones(len(d)-1)

w, v = eigh_tridiagonal(d, e)

plt.figure(figsize=(10,5))
plt.plot(y, mL2V(y),lw=10)
plt.title('Potential', fontsize=30)
plt.ylabel('$V/V_0$', fontsize=25)
plt.xlabel('$x/L$', fontsize=25)
plt.grid()
plt.savefig('v3p1.png', dpi=200)

plt.figure(figsize=(10,5))
plt.plot(y[1: -1], v.T[0]**2)
plt.plot(y[1: -1], v.T[1]**2)
plt.plot(y[1: -1], v.T[2]**2)
plt.plot(y[1: -1], v.T[3]**2)
plt.title('Eigenstates', fontsize=30)
plt.ylabel('$\psi$', fontsize=25)
plt.xlabel('$x/L$', fontsize=25)
plt.grid()
plt.savefig('v3p2.png', dpi=200)

plt.bar(np.arange(0, 10, 1), w[0:10])
plt.ylabel('$mL^2 E/\hbar^2$')
plt.savefig('v3p3.png', dpi=200)
