from vector import Vector

v1 = Vector([3.039, 1.879])
b1 = Vector([0.825, 2.036])

v2 = Vector([-9.88, -3.264, -8.159])
b2 = Vector([-2.155, -9.353, -9.473])

v3 = Vector([3.009, -6.172, 3.692, -2.51])
b3 = Vector([6.404, -9.144, 2.759, 8.718])

print('first pair...')
print('The projection of v on b is', round(v1.proj(b1), 3))

print('\nsecond pair...')
print('The orthogonal of v on b is:', round(v2.ortho(b2), 3))

print('\nthird pair...')
print('The projection of v on b is', round(v3.proj(b3), 3))
print('The orthogonal of v on b is:', round(v3.ortho(b3), 3))