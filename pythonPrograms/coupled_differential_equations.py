#Coupled Differential Equations

import numpy as np
import matplotlib.pyplot as plt


w=1.0

def rFxn(r,t):
    x= r[0]
    y= r[1]
    xFxn=x*y - x
    yFxn=y - x*y +np.sin(w*t)**2
    return np.array([xFxn, yFxn], float)

a,b,N=0.0, 10.0, 1000
h=(b-a)/N
r=np.array([1.0, 1.0], float)#initial condition



tPoints=np.linspace(a,b,N)
xList=[]
yList=[]

for t in tPoints:
    xList.append(r[0])
    yList.append(r[1])
    r+= h*rFxn(r,t)
    


plt.plot(tPoints, xList)
plt.plot(tPoints, yList)
plt.grid(True)
plt.show()
