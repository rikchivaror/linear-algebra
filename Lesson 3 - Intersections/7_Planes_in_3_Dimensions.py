from vector import Vector
from plane import Plane

p_11 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
p_12 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)

p_21 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
p_22 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)

p_31 = Plane(Vector([-7.926, 8.625, -7.212]), -7.952)
p_32 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)

print('Planes are equal:')
print('p_11 and p_12: ' + str(p_11 == p_12))
print('p_21 and p_22: ' + str(p_21 == p_22))
print('p_31 and p_32: ' + str(p_31 == p_32))

print('\nPlanes are parallel but not equal:')
print('p_11 and p_12: ' + str(p_11.is_parallel(p_12) and p_11 != p_12))
print('p_21 and p_22: ' + str(p_21.is_parallel(p_22) and p_21 != p_22))
print('p_31 and p_32: ' + str(p_31.is_parallel(p_32) and p_31 != p_32))

print('\nPlanes are parallel but not equal:')
print('p_11 and p_12: ' + str(not p_11.is_parallel(p_12)))
print('p_21 and p_22: ' + str(not p_21.is_parallel(p_22)))
print('p_31 and p_32: ' + str(not p_31.is_parallel(p_32)))