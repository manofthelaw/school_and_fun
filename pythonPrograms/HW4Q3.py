#HW4 Q3
#Jeremy Lampley

import numpy as np
from scipy.linalg import qr


A = np.array([[1,0,0],
              [1,1,0],
              [1,1,1]],float)
def QR_decomp(A):
    n, m = A.shape

    Q = np.zeros((n,n))
    R = np.zeros((n,m))
    U = np.zeros((n,n))

    #Set Q matrix

    U[:,0] = A[:,0]
    Q[:,0] = (U[:,0])/np.linalg.norm(U[:,0])

    for i in range(1,n):

        U[:,i] = A[:,i]
        for j in range(i):
            
            U[:,i] -= (A[:,i]@Q[:,j])*Q[:,j]

        Q[:,i] = U[:,i]/np.linalg.norm(U[:,i])

    for i in range(n):
        for j in range(i, m):
            R[i,j] = A[:,j] @ Q[:,i]
    return Q, R

def QR_eigvals(A, tol=1e-12, maxiter=1000):

    A_old = np.copy(A)
    A_new = np.copy(A)

    diff = np.inf
    i = 0
    while(diff > tol) and (i < maxiter):
        A_old[:, :] = A_new
        Q, R = QR_decomp(A_old)

        A_new[:, :] = R @ Q

        diff = np.abs(A_new - A_old).max()
        i +=1

    eigvals = np.diag(A_new)
    return eigvals

Q, R = QR_decomp(A)
print(Q)
print(R)
print(Q@R)
print("\n")

q, r = np.linalg.qr(A)
print(q)
print(r)
print(q@r)
print("\n")

print(QR_eigvals(A))
