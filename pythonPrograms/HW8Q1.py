#HW8Q1
#Jeremy Lampley

import numpy as np
import matplotlib.pyplot as plt
import random as rng



j = 0
N = 1000000

for i in range(N):
    dice1 = rng.randrange(1,7)
    dice2 = rng.randrange(1,7)
    if dice1 == 6 and dice2 == 6:
        j += 1
        #print(j, " current matches")
    #print(dice1, "dice one")
    #print(dice2, "dice two")


print(1/36, "Expected value")
print(j/N, "Matches per number of rolls")
