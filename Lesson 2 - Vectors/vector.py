import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    # -----------------------------------------------------------------------------
    # is_parallel(self, other):
    #   Determine if two vectors are parallel. They are parallel of is a scalar
    #   multiple of the other or if at least one vector is the zero vector.
    #
    # Arguments:
    #   self, other: objects of the Vector class
    #
    # Returns:
    #   the 'bool' type based on whether the vectors are parallel or not
    def is_parallel(self, other):
        if self.is_zero() or other.is_zero():
            return True

        self_unit_vec = round(self.get_unit_vec(), 3)
        other_unit_vec = round(other.get_unit_vec(), 3)

        return self_unit_vec == other_unit_vec or self_unit_vec == other_unit_vec.scalar_mult(-1)

    def is_zero(self):
        for e in self.coordinates:
            if e:
                return False
        return True

    # -----------------------------------------------------------------------------
    # is_ortho(self, other):
    #   Determine if two vectors are orthogonal. The vectors are orthogonal if the
    #   dot products of the vectors is zero.
    #
    # Arguments:
    #   self, other: objects of the Vector class
    #
    # Returns:
    #   the 'bool' type based on whether the vectors are orthogonal or not
    def is_ortho(self, other):
        if round(self.dot_product(other), 3):
            return False
        return True

    def dot_product(self, other):
        y = 0
        for i in range(self.dimension):
            y += self.coordinates[i] * other.coordinates[i]
        return y

    def get_angle(self, other):
        u1 = self.get_unit_vec()
        u2 = other.get_unit_vec()

        try:
            return math.acos(round(u1.dot_product(u2), 5))

        except ZeroDivisionError:
            raise Exception("Cannot compute an angle with the zero vector")

    def scalar_mult(self, c):
        x = []
        for e in self.coordinates:
            x.append(c * e)
        return Vector(x)

    def get_mag(self):
        x = 0
        for e in self.coordinates:
            x += e ** 2
        return x ** 0.5

    def get_unit_vec(self):
        try:
            return self.scalar_mult(1/self.get_mag())

        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        sum = []
        for i in range(self.dimension):
            sum.append(self.coordinates[i] + other.coordinates[i])
        return Vector(sum)

    def __sub__(self, other):
        sum = []
        for i in range(self.dimension):
            sum.append(self.coordinates[i] - other.coordinates[i])
        return Vector(sum)

    def __mul__(self, other):
        prod = []
        for i in range(self.dimension):
            prod.append(self.coordinates[i] * other)
        return Vector(prod)

    def __round__(self, n=None):
        rounded = []
        for i in range(self.dimension):
            rounded.append(round(self.coordinates[i], n))
        return Vector(rounded)


def test():
    vector_1 = Vector([1, 2, -1])
    vector_2 = Vector([3, 1, 0])
    vector_3 = vector_2.scalar_mult(math.pi)
    vector_4 = Vector([0, 0, 0])
    vector_5 = Vector([3, 4, 11])

    ### test for __eq__() method
    # print(vector_1 == vector_2)

    ### test is_zero() method
    # print(vector_1.is_zero())
    # print(vector_4.is_zero())

    ### test for dot_product() method
    # print(vector_1.dot_product(vector_2))

    ### test for .get_angle() method
    # print((vector_1.get_angle(vector_2)))
    # print((vector_2.get_angle(vector_3)))
    # print((vector_1.get_angle(vector_4)))

    ### test for is_parallel() method
    print(vector_1.is_parallel(vector_2))
    print(vector_2.is_parallel(vector_3))
    print(vector_3.is_parallel(vector_2))
    print(vector_3.is_parallel(vector_4))
    print(vector_4.is_parallel(vector_3))

    ### test for is_ortho() method
    # print(vector_1.is_ortho(vector_5))
    # print(vector_1.is_ortho(vector_4))
    # print(vector_5.is_ortho(vector_1))
    # print(vector_4.is_ortho(vector_1))
    # print(vector_1.is_ortho(vector_2))


if __name__ == '__main__':
    test()
