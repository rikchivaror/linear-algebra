from vector import Vector

# vectors are parallel
v3 = Vector([-7.579, -7.88])
v4 = Vector([22.737, 23.64])

# vectors are not parallel or orthogonal
v5 = Vector([-2.029, 9.97, 4.172])
v6 = Vector([-9.231, -6.639, -7.245])

# vectors are orthogonal
v7 = Vector([-2.328, -7.284, -1.214])
v8 = Vector([-1.821, 1.072, -2.94])

# vectors are parallel and orthogonal
v9 = Vector([2.118, 4.827])
v10 = Vector([0, 0])

print('first pair...')
print('is parallel:', v3.is_parallel(v4))
print('is orthogonal:', v3.is_orthogonal(v4))

print('\nsecond pair...')
print('is parallel', v5.is_parallel(v6))
print('is orthogonal:', v5.is_orthogonal(v6))

print('\nthird pair...')
print('is parallel', v7.is_parallel(v8))
print('is orthogonal:', v7.is_orthogonal(v8))

print('\nfourth pair...')
print('is parallel', v9.is_parallel(v10))
print('is orthogonal:', v9.is_orthogonal(v10))





