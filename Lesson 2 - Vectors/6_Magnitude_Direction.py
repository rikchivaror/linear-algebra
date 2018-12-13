from vector import Vector

vector1 = Vector([-0.221, 7.437])
vector2 = Vector([8.813, -1.331, -6.247])
vector3 = Vector([5.581, -2.136])
vector4 = Vector([1.996, 3.108, -4.554])
# vector5 = Vector([0, 0])

print(round(vector1.get_mag(), 3))
print(round(vector2.get_mag(), 3))
print(round(vector3.get_unit_vec(), 3))
print(round(vector4.get_unit_vec(), 3))
# print(round(vector5.get_unit_vec(), 3))

