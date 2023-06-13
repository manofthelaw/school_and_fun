#HW 3 Question 1
#Trapezoidal and Simpson Rules
#Jeremy lampley

import numpy as np
import matplotlib.pyplot as plt



def fxn(x):
    return x**4-2*x+1

#Input Parameters
a,b,N=0.0,2.0,100
y= np.linspace(a,b,N)

#step size
h=(b-a)/N

#Trapezoidal Integration

tIntegral=0.0
for k in range(1,N):
    tIntegral+=fxn(a+k*h)
tIntegral+=0.5*(fxn(a))
tIntegral+=0.5*(fxn(b))
tIntegral=h*tIntegral

#Simpson Integration

sIntegral=0.0
for k in range(1,N):
    if k%2==0:
        sIntegral+=2*fxn(a+k*h)
    else:
        sIntegral+=4*fxn(a+k*h)
sIntegral+=fxn(a)+fxn(b)
sIntegral*=h/3

#Plotting the function
plt.plot(y, fxn(y))
plt.axis([0, 2, -1, 10])
plt.grid(True)
plt.show()

print("Trapezoidal: ", tIntegral)
print("Simpson's: ", sIntegral)


