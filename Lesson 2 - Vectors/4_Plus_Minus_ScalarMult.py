from vector import Vector

vector_1a = Vector([8.218, -9.341])
vector_1b = Vector([-1.129, 2.111])

vector_2a = Vector([7.119, 8.215])
vector_2b = Vector([-8.223, 0.878])

vector_3a = Vector([1.671, -1.012, -0.318])

print(round(vector_1a + vector_1b, 3))
print(round(vector_2a - vector_2b, 3))
print(round(vector_3a.scalar_mult(7.41), 3))
