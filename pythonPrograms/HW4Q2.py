#Jeremy Lampley
#Homework 4 Question 2

import numpy as np
import matplotlib.pyplot as plt

#Matrix
A= np.array([[2, 1, 4, 1],
             [3, 4, -1, -1],
             [1, -4, 1, 5],
             [2, -2, 1, 3]], float)
v= np.array([-4, 3, 9, 7], float)
N= len(v)

I= np.array([[1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]], float)
L= I.copy()
U = A.copy()


for m in range(N):
    L[m+1:,m] = U[m+1:,m]/ U[m,m]
   
    
    for i in range(m+1, N):
        U[i:] = U[i:] - U[m]*(U[i,m]/U[m,m])


y=np.zeros(N,float)
x= np.zeros(N, float)

y[0] = v[0] / L[0,0]

for i in range (1,N):
    y[i] = (v[i] - np.dot(L[i,:i],y[:i]))/L[i,i]

    
x[-1] = y[-1]/ U[-1,-1]

for i in range(N-2, -1, -1):
    x[i] = (y[i] - np.dot(U[i,i:],x[i:]))/U[i,i]
      
        
print("L= \n",L,"\n")
print("U= \n",U,"\n")
print("A= \n",L@U,"\n")
print("y= \n",y,"\n")
print("x= \n",x,"\n")

print(np.linalg.solve(A, v))



