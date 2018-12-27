from vector import Vector
from line import Line

l_11 = Line(Vector([4.046, 2.836]), 1.21)
l_12 = Line(Vector([10.115, 7.09]), 3.025)

l_21 = Line(Vector([7.204, 3.182]), 8.68)
l_22 = Line(Vector([8.172, 4.114]), 9.883)

l_31 = Line(Vector([1.182, 5.562]), 6.744)
l_32 = Line(Vector([1.773, 8.343]), 9.525)

print('Intersection of first pair of lines is:')
print(l_11.get_intersection(l_12))

print('\nIntersection of second pair of lines is:')
print(l_21.get_intersection(l_22))

print('\nIntersection of third pair of lines is:')
print(l_31.get_intersection(l_32))
