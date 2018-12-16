from vector import Vector
from math import degrees

v1 = Vector([-7.579, -7.88])
w1 = Vector([22.737, 23.64])
v2 = Vector([-2.029, 9.97, 4.172])
w2 = Vector([-9.231, -6.639, -7.245])
v3 = Vector([-2.328, -7.284, -1.214])
w3 = Vector([-1.821, 1.072, -2.94])
v4 = Vector([2.118, 4.827])
w4 = Vector([0, 0])

print(degrees(v1.get_angle(w1)))
print(v1.is_parallel(w1))
print(v1.is_ortho(w1))

print(degrees(v2.get_angle(w2)))
print(v2.is_parallel(w2))
print(v2.is_ortho(w2))

print(degrees(v3.get_angle(w3)))
print(v3.is_parallel(w3))
print(v3.is_ortho(w3))


print(v4.is_parallel(w4))
print(v4.is_ortho(w4))

