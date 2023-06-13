#ROmberg Integration
#Thushari Jayasekera Jan 31st 2022
# Please note.. This is not an optimized code
import numpy as np


#Function
def fxn(x):
    return (np.sin(np.sqrt(100*x))**2)
#Input Parameters
a,b=0.0,1
Nstart,maxNstep=5,6

#Trapazoidal Integral
def trzintfxn(N):
    h=(b-a)/N
    trz_int=0.5*(fxn(a)+fxn(b))
    for k in range(1,N):
        trz_int+=fxn(a+k*h)
    trz_int*=h
    return trz_int

#Romber Loop
romberg=np.zeros([maxNstep,maxNstep],float)
for i in range(maxNstep):
    romberg[i,0]=trzintfxn(Nstart*2**i) #Trapazoidal Steps
    print(i,"*****")
    for m in range(1,i+1): # Romberg Steps
        print(i,"  ",m)
        romberg[i,m]=romberg[i,m-1]+(1/(4**m-1))*(romberg[i,m-1]-romberg[i-1,m-1])
        #print("Error: ", ((b-a)/(Nstart*2**i))**(2*m+2), "i= ", i)
print(romberg)          
