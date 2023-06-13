#HW5Q3
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt

def fxn(f, t):
    x = f[0]
    y = f[1]
    z = f[2]
    fx = sigma *(y - x)
    fy = r * x - y - x * z
    fz = x * y - b * z
    return np.array([fx, fy, fz], float)

a, b, N = 0.0, 50.0, 10000
h=(b-a)/N
tPoints = np.linspace(a,b,N)
sigma = 10
r = 28
b = 8/3

def rk4(tPoints, h, fxn):
    xList = []
    yList = []
    zList = []
    f = np.array([0.0, 1.0, 0.0], float)#initial condition
    
    for t in tPoints:
        xList.append(f[0])
        yList.append(f[1])
        zList.append(f[2])
        j1=h*fxn(f, t)
        j2=h*fxn(f+0.5*j1, t+0.5*h)
        j3=h*fxn(f+0.5*j2, t+0.5*h)
        j4=h*fxn(f+j3, t+h)
        f += (j1+2*j2+2*j3+j4)/6

    

    return xList, yList, zList

x,y,z = rk4(tPoints, h, fxn)
plt.plot(tPoints, y)
plt.grid(True)
plt.show()

plt.plot(z, x, lw = 0.5)
plt.grid(True)
plt.show()
plt.show()

plt.plot(x, z, lw = 0.5)
plt.grid(True)
plt.show()
plt.show()

plt.plot(x, y, lw = 0.5)
plt.grid(True)
plt.show()
plt.show()

plt.plot(y, x, lw = 0.5)
plt.grid(True)
plt.show()
plt.show()

plt.plot(y, z, lw = 0.5)
plt.grid(True)
plt.show()
plt.show()

plt.plot(z, y, lw = 0.5)
plt.grid(True)
plt.show()
plt.show()

    
