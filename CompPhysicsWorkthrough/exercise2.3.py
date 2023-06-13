#Exercise 2.3
#including the example 2.2(converting polar to cartesian)
#convert polar coordinates to cartesian coordinates

import numpy as np

#initial example

r = float(input("Enter r: "))
d = float(input("Enter theta in degrees: "))

#calculate
theta = d * np.pi / 180
x = r * np.cos(theta)
y = r * np.sin(theta)

print("x = ", x, "y= ", y)

#now the exercise
#take in x and y coordinates and give the polar coordinates back

x = float(input("Enter x: "))
y = float(input("Enter y: "))

#calculate
r = np.sqrt(x**2 + y**2)
theta = np.arctan(y/x) * 180 / np.pi

print("r= ", r, "theta= ", theta, " degrees.")
