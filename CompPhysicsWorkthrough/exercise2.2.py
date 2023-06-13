#Exercise 2.2
#Altitude of a satellite
import numpy as np

#Define constants
G = 6.67 * 10 ** -11 # m**3 kg**-1 s**-2
M = 5.97 * 10 ** 24 # kg
R = 6371 * 1000 # m

#Take input for the period from user.
T = float(input("Enter the period for the satellite(seconds): "))


#Altitude calculation from Kepler's third law.
h = np.cbrt(G * M * T**2 / (4*np.pi**2)) - R

print("The altitude of the satellite with a period of ", T, "seconds is", h/1000, "kilometers.")
