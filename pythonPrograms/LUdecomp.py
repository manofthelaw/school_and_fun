import numpy as np

#L = np.array([[1,0,0],
              #[2,1,0],
              #[3,4,1]])
#U = np.array([[1,1,0],
              #[0,-1,-1],
              #[0,0,3]])

#print(L @ U)

def lu(A):
    n = A.shape[0]

    U = A.copy()
    L = np.eye(n, dtype=np.double)

    #Loop over rows
    for i in range(n):

        #Eliminate entries below i with row operations
        #on U and reverse the row operations to
        #manipulate L
        factor = U[i+1:, i] / U[i,i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]

    return  L, U, L @ U

A= np.array([[2, 1, 4, 1],
             [3, 4, -1, -1],
             [1, -4, 1, 5],
             [2, -2, 1, 3]], float)

print("L= \n",lu(A)[0], "\n")
print("U= \n",lu(A)[1], "\n")
print("A= \n",lu(A)[2], "\n")
