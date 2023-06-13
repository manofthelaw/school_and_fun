#spaceship travel time

import numpy as np

#constants
c = 299792458 #m/s

#take input for x and v as a fraction of the speed of light c

x = float(input("Enter the distance of the planet in light years: "))
v = float(input("Enter the speed of the spaceship as fraction of the speed of light: "))

#calculate
light_year =  9460730472580800 * x
t = (light_year / (v * c)) / (3600)

print(t, " hours.")
print(t/24, " days.")
print(t/(24*365), " years.")

#satur V speed is ~0.0000207 of the speed of light
