
#Import keseluruhan module
#import math
# Hanya import pi dari module math
from math import pi
from math import sqrt
# Definition of radius
r = 0.43

# Calculate C
C = 2 * pi * r

# Calculate A (In Python **2)
A = pi * r**2

print(C)
print(A)

# (-b +- / 4ac) / (2a)
# x^2 - x+ 3 = 0
a = 1
b = -1
c = 3
x1 = -b + (sqrt(4*a*c)/(2*a))
x2 = -b - (sqrt(4*a*c)/(2*a))

print(x1)
print(x2)