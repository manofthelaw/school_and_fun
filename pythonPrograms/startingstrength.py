#STarting Strength calculator

import numpy as np

#starting weights
squat = 135
bench = 95
deadlift = 185
press = 45

A = 1
B = 0

#workout A or B
while squat < 205:
    if A == 1:
        squat += 10
        bench += 5
        deadlift += 10
        A, B = 0, 1
    else:
        squat += 10
        press += 5
        deadlift += 10
        A, B = 1, 0

print("squat: ", squat, "\nbench: ", bench, "\npress: ", press, "\ndeadlift: ", deadlift)
