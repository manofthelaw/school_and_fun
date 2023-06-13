#Euler, RK2, RK4 Method

import numpy as np
import matplotlib.pyplot as plt

x,y,z=[0.0],[0.0],[0.0]
a,b,N=0.0,20.0,100
h=(b-a)/N

def fxn(x,t):
    return -x**3 + np.sin(t)

tPoints=np.linspace(a,b,N)

#Euler method
for t in tPoints[1:]:
    x.append(x[-1]+ h*fxn(x[-1], t))


#RK2 method
for t in tPoints[1:]:
    k1=h*fxn(y[-1], t)
    k2=h*fxn(y[-1]+0.5*k1, t+0.5*h)
    y.append(y[-1]+ k2)

#RK4 method
for t in tPoints[1:]:
    j1=h*fxn(z[-1], t)
    j2=h*fxn(z[-1]+0.5*j1, t+0.5*h)
    j3=h*fxn(z[-1]+0.5*j2, t+0.5*h)
    j4=h*fxn(z[-1]+j3, t+h)
    z.append(z[-1] + (1/6)*(j1+ 2*j2 + 2*j3 + j4))

plt.plot(tPoints, x)
plt.plot(tPoints, y)
plt.plot(tPoints, z)
plt.grid(True)
plt.show()
