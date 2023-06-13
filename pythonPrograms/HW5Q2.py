#HW5Q2
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt

g = 9.81
l = 0.1

def fxn(r,t):
    theta = r[0]
    omega = r[1]
    fTheta = omega
    fOmega = -(g/l)*np.sin(theta)
    return np.array([fTheta,fOmega],float)

a,b,N=0.0, 10.0, 1000
h=(b-a)/N
initial_angle = 150.0
tPoints = np.linspace(a,b,N)


def rk4(tPoints, h, initial_angle , fxn):
    thetaList = []
    omegaList = []
    r=np.array([np.radians(initial_angle), 0.0], float)#initial condition
    
    for t in tPoints:
        thetaList.append(r[0])
        omegaList.append(r[1])
        j1=h*fxn(r, t)
        j2=h*fxn(r+0.5*j1, t+0.5*h)
        j3=h*fxn(r+0.5*j2, t+0.5*h)
        j4=h*fxn(r+j3, t+h)
        r += (j1+2*j2+2*j3+j4)/6

    for i in range(len(thetaList)):
        thetaList[i] *= (180/np.pi)

    for i in range(len(omegaList)):
        omegaList[i] *= (180/np.pi)

    return thetaList, omegaList

def rk2(tPoints, h, initial_angle, fxn):
    thetaList = []
    omegaList = []
    r=np.array([np.radians(initial_angle), 0.0], float)#initial condition

    for t in tPoints:
        thetaList.append(r[0])
        omegaList.append(r[1])
        k1=h*fxn(r, t)
        k2=h*fxn(r+0.5*k1, t+0.5*h)
        r += k2

    for i in range(len(thetaList)):
        thetaList[i] *= (180/np.pi)
    for i in range(len(omegaList)):
        omegaList[i] *= (180/np.pi)

    return thetaList, omegaList
    
def euler(tPoints, h, initial_angle, fxn):
    thetaList = []
    omegaList = []
    r=np.array([np.radians(initial_angle), 0.0], float)#initial condition
    
    for t in tPoints:
        thetaList.append(r[0])
        omegaList.append(r[1])
        r += h*fxn(r,t)
        
    for i in range(len(thetaList)):
        thetaList[i] *= (180/np.pi)
    for i in range(len(omegaList)):
        omegaList[i] *= (180/np.pi)
        
    return thetaList, omegaList
    

theta, omega = euler(tPoints, h, initial_angle, fxn)
plt.plot(theta, omega)
plt.title("Euler method")
plt.grid(True)
plt.savefig('euler001.jpg', dpi=100)
plt.show()


theta, omega = rk2(tPoints, h, initial_angle, fxn)
plt.plot(theta,omega)
plt.title("RK2 method")
plt.grid(True)
#plt.savefig('rk2_001.jpg', dpi=100)
plt.show()


theta, omega = rk4(tPoints, h, initial_angle, fxn)
plt.plot(theta,omega)
plt.title("RK4 method")
plt.grid(True)
#plt.savefig('rk4_001_150deg.jpg', dpi=100)
plt.show()






