#HW7Q3
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt

h = 1e-18
hbar = 1.0546e-34
L = 1e-8
M = 9.109e-31
N = 1000 # Grid slices

a = L/N

def complex_arg(trans):	
	def f(y):
		return trans(np.real(y)) + 1j*trans(np.imag(y))

	return f
    
@complex_arg
def dst(y):
    """
	Perform dst transform for real argument
    """
    N = len(y)
    y2 = np.empty(2*N,float)
    y2[0] = y2[N] = 0.0
    y2[1:N] = y[1:]
    y2[:N:-1] = -y[1:]
    a = -np.imag(np.fft.rfft(y2))[:N]
    a[0] = 0.0

    return a

@complex_arg
def idst(a):
    N = len(a)
    c = np.empty(N+1,complex)
    c[0] = c[N] = 0.0
    c[1:N] = -1j*a[1:]
    y = np.fft.irfft(c)[:N]
    y[0] = 0.0

    return y

psi = np.zeros(N+1,complex)

def psi0(x):
	x0 = L/2
	sigma = 1e-10
	k = 5e10
	return np.exp(-(x-x0)**2/2/sigma**2)*np.exp(1j*k*x)

x = np.linspace(0,L,N+1)
psi[:] = psi0(x)
psi[[0,N]]=0

b0 = dst(psi)

t = 1e-18
b_ = b0*np.exp(1j*np.pi**2*hbar*np.arange(1,N+2)**2/2/M/L**2*t)

psi_ = idst(b_)
plt.plot(psi_.real)
plt.show()


for timestep in range(2000):
    
    b_ = b0*np.exp(-1j*np.pi**2*hbar*np.arange(1,N+2)**2/2/M/L**2*timestep*h) 
    psi_ = idst(b_)
    prob = (psi_*np.conj(psi_))

    plt.ylim(-1,1)
    plt.plot(psi_.real)
    #plt.plot(prob.real)
    plt.pause(0.0001)
    plt.cla()
plt.show()
