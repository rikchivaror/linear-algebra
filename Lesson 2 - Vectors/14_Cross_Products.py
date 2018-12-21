from vector import Vector

v_1 = Vector([8.462, 7.893, -8.187])
w_1 = Vector([6.984, -5.975, 4.778])

v_2 = Vector([-8.987, -9.838, 5.031])
w_2 = Vector([-4.268, -1.861, -8.866])

v_3 = Vector([1.5, 9.547, 3.691])
w_3 = Vector([-6.007, 0.124, 5.772])

# vectors are parallel
v_4 = Vector([-7.579, -7.88])
w_4 = Vector([22.737, 23.64])

v_5 = Vector([3, 3])
w_5 = Vector([4.5, 4.5])

# vectors are orthogonal
v_6 = Vector([-2.328, -7.284, -1.214])
w_6 = Vector([-1.821, 1.072, -2.94])


print('first pair...')
print('The cross product of v and w is', round(v_1.cross_prod(w_1), 3))

print('\nsecond pair...')
print('The area of the parallelogram spanned by v and w is:', round(v_2.area_parallelogram(w_2), 3))

print('\nthird pair...')
print('The area of the triangle spanned by v and w is:', round(v_3.area_triangle(w_3), 3))

print('\nfourth pair...')
print('The cross product of v and w is', round(v_4.cross_prod(w_4), 3))

print('\nfifth pair...')
print('The cross product of v and w is', round(v_5.cross_prod(w_5), 3))

print('\nsixth pair...')
print('The cross product of v and w is', round(v_6.cross_prod(w_6), 3))