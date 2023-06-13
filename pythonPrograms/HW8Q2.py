#HW8Q2
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt
import random as rng

Bi213 = 10000
Tl = 0
Pb = 0
Bi209 = 0
h = 1.0
Bi213Tau = 46*60
TlTau = 2.2*60
PbTau = 3.3*60
pTl = 1 - 2**(-h/TlTau)
p213 = 1 - 2**(-h/Bi213Tau)
pPb = 1 - 2**(-h/PbTau)

tmax = 20000

Bi213List = []
TlList = []
PbList= []
Bi209List = []

tPoints = np.arange(0, tmax, h)

for t in tPoints:
    Bi209List.append(Bi209)
    PbList.append(Pb)
    TlList.append(Tl)
    Bi213List.append(Bi213)
    

    
    for i in range(Pb):
        if rng.random()<pPb:
            Bi209 += 1
            Pb -= 1
    
    for i in range(Tl):
        if rng.random()<pTl:
            Tl -= 1
            Pb += 1
    
    for i in range(Bi213):
        if rng.random()<p213:
            Bi213 -= 1
            if rng.random()<0.9791:
                Pb += 1 
            else:
                Tl += 1
             
    
    
    


fig, ax = plt.subplots()
ax.plot(tPoints,Bi213List, label='Bi213')
ax.plot(tPoints,TlList, label='Ti')
ax.plot(tPoints,PbList, label='Pb')
ax.plot(tPoints,Bi209List, label='Bi209')
legend = ax.legend(loc='center', shadow=True, fontsize='x-large')
plt.show()
