from vector import Vector
import math

v1 = Vector([7.887, 4.138])
w1 = Vector([-8.802, 6.776])

v2 = Vector([-5.955, -4.904, -1.874])
w2 = Vector([-4.496, -8.755, 7.103])

v3 = Vector([3.183, -7.627])
w3 = Vector([-2.668, 5.319])

v4 = Vector([7.35, 0.221, 5.188])
w4 = Vector([2.751, 8.259, 3.985])

print(round(v1.dot_product(w1), 3))
print(round(v2.dot_product(w2), 3))
print(round(v3.get_angle(w3), 3))
print(round(math.degrees(v4.get_angle(w4)), 3))
