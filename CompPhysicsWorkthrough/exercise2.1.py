#Example 2.1
#A ball dropped from a tower
#A program that calculates the height of a ball above ground after given a height h and a time t.

#imports
from numpy import *


#Input height by user.
h = float(input("Enter the height of the tower(meters): "))

#Input time interval by user.
t = float(input("Enter the time interval(seconds): "))

#Standard kinematic formula for falling object.
g = 9.81
s = g * t ** 2 / 2

#Print result of the calculation.
print("The height of the ball is:", h-s, "meters.")

#Solve the time it takes for a ball to hit the ground.
h = float(input("Enter the height of the tower(meters): "))

#Equation to find the time it takes for the ball to hit the ground.
t = sqrt(2 * h / g)

print("The time it takes for the ball to hit the ground is:", t, "seconds.")
