#vpython test

from vpython import sphere,rate,vector
from math import cos,sin,pi
from numpy import arange

s = sphere(pos=vector(1,0,0), radius =0.1)
for theta in np.arange(0, 10*np.pi, 0.1):
    rate(60)
    x = np.cos(theta)
    y = np.sin(theta)
    s.pos = vector(x, y, 0)
