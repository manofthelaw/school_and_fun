# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 06:47:08 2013
@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *

N = 10000000

z = random(N)
print(z)
x = z**2
print(x)

def g(x):
	
	return 1/(1+exp(x))

I = sum(g(x))/N*2


print('I = {}'.format(I))
