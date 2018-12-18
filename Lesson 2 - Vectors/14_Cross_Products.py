from vector import Vector

v_1 = Vector([8.462, 7.893, -8.187])
w_1 = Vector([6.984, -5.975, 4.778])

v_2 = Vector([-8.987, -9.838, 5.031])
w_2 = Vector([-4.268, -1.861, -8.866])

v_3 = Vector([1.5, 9.547, 3.691])
w_3 = Vector([-6.007, 0.124, 5.772])

print('first pair...')
print('The cross product of v and b is', round(v_1.cross_prod(w_1), 3))

print('\nsecond pair...')
print('The area of the parallelogram spanned by v and w is:', round(v_2.area_parallelogram(w_2), 3))

print('\nthird pair...')
print('The area of the triangle spanned by v and w is:', round(v_3.area_triangle(w_3), 3))

# TODO: test case where either v or w are parallel (ang = 0 or 180)
# TODO: test cases where v and w
