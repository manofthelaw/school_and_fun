#HW8Q3
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt
import random as rng

N = 1000000

z = []
for i in range(N):
    z.append(rng.random()**2)


def func(x):
    return 1/(1+np.exp(x))

integral = sum(func(z))/N*2

print('Integral = {}'.format(integral))
