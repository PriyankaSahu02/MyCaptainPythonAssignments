# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 16:50:23 2023

@author: PriyankaSahu5
"""

# import math module
from math import pi

# take input from user
r = float(input ("Input the radius of the circle:"))

# compute the area from radius of a circle given by a user 
calculateArea = str(pi * r**2);

#print result
print ("The Area of the circle with radius " + str(r) + "is:" + calculateArea)
