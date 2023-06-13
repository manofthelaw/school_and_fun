#This Code is written by Thushari Jayasekera
#2022 Spring 476C class

import scipy.integrate

N=10
a,b=0.0,2.0
h=(b-a)/N
integral=0.0
def fxn(x):
    return x**4-2*x+1
for k in range(1,N):
    if k%2==0:
        integral+=2*fxn(a+k*h)
    else:
        integral+=4*fxn(a+k*h)
integral+=fxn(a)+fxn(b)
integral*=h/3

