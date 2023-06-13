#Jeremy Lampley
#Homework 4 Question 1

import numpy as np
import matplotlib.pyplot as plt

#Matrix
A= np.array([[2, 1, 4, 1],
             [3, 4, -1, -1],
             [1, -4, 1, 5],
             [2, -2, 1, 3]], float)
v= np.array([-4, 3, 9, 7], float)
N= len(v)


for m in range(N):
    d = A[m,m]
    A[m,:] /= d
    v[m] /= d
    

    for i in range(m+1, N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

x= np.empty(N, float)
for m in range (N-1, -1, -1):
    x[m] = v[m]
    for i in range(m+1, N):
        x[m] -= A[m,i]*x[i]

print(x)
