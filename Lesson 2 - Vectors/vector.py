import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple(Decimal(x) for x in coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    # -----------------------------------------------------------------------------
    # is_ortho(self, other):
    #   Determine if two vectors are orthogonal. The vectors are orthogonal if the
    #   dot products of the vectors is close to (within epsilon of) zero.
    #
    # Arguments:
    #   self, other: Vector objects
    #   epsilon: allowable tolerance between the result and value of zero
    #
    # Returns:
    #   the 'bool' type based on whether the vectors are orthogonal or not
    def is_ortho(self, other, epsilon=1e-10):
        return abs(self.dot_product(other)) < epsilon

    # -----------------------------------------------------------------------------
    # is_parallel(self, other):
    #   Determine if two vectors are parallel. This is done by calculating
    #   the normalized dot product. If the result is close to (within epsilon of) 1
    #   then the vectors are parallel.
    #
    # Arguments:
    #   self, other: Vector objects
    #   epsilon: allowable tolerance between the result and value of 1
    #
    # Returns:
    #   the 'bool' type based on whether the vectors are parallel or not
    def is_parallel(self, other, epsilon=1e-10):
        return (self.is_zero() or other.is_zero()
                or abs(abs(self.normalize().dot_product(other.normalize())) - 1) < epsilon)

    # -----------------------------------------------------------------------------
    # is_zero(self, other):
    #   Determine if the vector is the zero vector. The vector is the zero vector
    #   if it's magnitude is close to zero.
    #
    # Arguments:
    #   self: a Vector object
    #   epsilon: allowable tolerance between the result and value of zero
    #
    # Returns:
    #   the 'bool' type based on whether the vectors are parallel or not
    def is_zero(self, epsilon=1e-10):
        return self.get_mag() < epsilon

    def dot_product(self, other):
        y = 0
        for i in range(self.dimension):
            y += self.coordinates[i] * other.coordinates[i]
        return y

    def get_angle(self, other):
        u1 = self.normalize()
        u2 = other.normalize()
        return math.acos(u1.dot_product(u2))

    def scalar_mult(self, c):
        x = []
        for e in self.coordinates:
            x.append(Decimal(c) * e)
        return Vector(x)

    def get_mag(self):
        x = Decimal('0.0')
        for e in self.coordinates:
            x += e ** Decimal('2.0')
        return x ** Decimal('0.5')

    def normalize(self):
        try:
            return self.scalar_mult(Decimal('1.0')/self.get_mag())

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
    v1 = Vector([1, 2, -1])
    v2 = Vector([3, 1, 0])

    v3 = Vector([-7.579, -7.88])
    v4 = Vector([22.737, 23.64])

    v5 = Vector([-2.029, 9.97, 4.172])
    v6 = Vector([-9.231, -6.639, -7.245])

    v7 = Vector([-2.328, -7.284, -1.214])
    v8 = Vector([-1.821, 1.072, -2.94])

    v9 = Vector([2.118, 4.827])
    v10 = Vector([0, 0])

    # test for dot_product() method
    # print(v3.dot_product(v4))
    # print(v3.normalize().dot_product(v4.normalize()))
    # print(v7.normalize().dot_product(v8.normalize()))

    # test for get_angle() method
    # print(math.degrees(v3.get_angle(v4)))
    # print(math.degrees(v5.get_angle(v6)))
    # print(math.degrees(v7.get_angle(v8)))

    # test for is_ortho() method
    # print(v3.is_ortho(v4))
    # print(v5.is_ortho(v6))
    # print(v7.is_ortho(v8))
    # print(v9.is_ortho(v10))

    # test for is_ortho() method
    print(v3.is_parallel(v4))
    print(v5.is_parallel(v6))
    print(v7.is_parallel(v8))
    print(v9.is_parallel(v10))

if __name__ == '__main__':
    test()
