from vector import Vector

v3 = Vector([-7.579, -7.88])
v4 = Vector([22.737, 23.64])

v5 = Vector([-2.029, 9.97, 4.172])
v6 = Vector([-9.231, -6.639, -7.245])

v7 = Vector([-2.328, -7.284, -1.214])
v8 = Vector([-1.821, 1.072, -2.94])

v9 = Vector([2.118, 4.827])
v10 = Vector([0, 0])

# test for is_ortho() method
print(v3.is_ortho(v4))
print(v5.is_ortho(v6))
print(v7.is_ortho(v8))
print(v9.is_ortho(v10))

# test for is_parallel() method
print(v3.is_parallel(v4))
print(v5.is_parallel(v6))
print(v7.is_parallel(v8))
print(v9.is_parallel(v10))

