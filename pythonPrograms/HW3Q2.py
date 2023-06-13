#HW 3 Question 2
#Velocity and Distance
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt

t=[]
v=[]
x=[0]

f = open("velocities.txt", "r")
content = f.read()
content = content.replace('\t', '\n')
content_list = content.splitlines()
f.close()
#print(content_list)

i=0

while i < len(content_list):
        t.append(int(content_list[i]))
        #print("time", content_list[i])
        i+=1
        v.append(float(content_list[i]))
        #print("velocity", content_list[i])
        i+=1

j=1

while j < len(t):
        x.append((v[j])*(t[j]))
        j+=1
        
        


h = ((int(t[100])-int(t[0]))/len(t))

#Trapezoidal Integration

tIntegral=0.0
for k in range(1,len(t)):
    tIntegral+= v[k]
tIntegral+=v[0]*0.5
tIntegral+=v[100]*0.5
tIntegral=h*tIntegral

print("Integral=",tIntegral)

plt.plot(t, v)
plt.grid()
plt.show()


plt.plot(t, x)
plt.grid()
plt.show()

#checking how close I am
#import scipy.integrate

#print(scipy.integrate.simpson(v))
#print(scipy.integrate.trapezoid(v))

