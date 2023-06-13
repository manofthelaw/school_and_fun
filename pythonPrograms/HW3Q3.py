#Homework 3 Question 3
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt
import math

#Given Function
def fxn(x):
    return (np.sin(np.sqrt(100*x))**2)


a,b,N=0.0,1.0,100
y = np.linspace(a,b,N)
nStart,nStep=5,6


#Plot
plt.plot(y, fxn(y))
plt.grid(True)
plt.show()

def error(m,N):
    return ((b-a)/(N))**(2*m+2)
    

#Trapezoidal Integration
def trapezoidal(N):
    h=(b-a)/N
    trz_int=0.5*(fxn(a)+fxn(b))
    for k in range(1,N):
        trz_int+=fxn(a+k*h)
    return (trz_int*h)

#Romberg Method
romberg=np.zeros([nStep, nStep], float)
for i in range(nStep):
    romberg[i,0]=trapezoidal(nStart*2**i)
                                
    for m in range(1,i+1):
        romberg[i,m]=romberg[i,m-1]+(1/(4**m-1))*(romberg[i,m-1]-romberg[i-1,m-1])
        print("i:", i, "\tm:", m, "\tError=", error(m,nStart*2**i))

print(romberg)

#not so sure about my error calculation. 
