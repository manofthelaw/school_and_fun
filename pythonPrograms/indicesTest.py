

import numpy as np
import matplotlib.pyplot as plt


A = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

newA = np.zeros(len(A))
print(newA)
print(len(A))
print(int(0.2*len(A)))

newA = A[:int(0.2*len(A))]
print(newA)
