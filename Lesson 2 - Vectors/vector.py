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
    def proj(self, basis):
        unit_b = basis.normalize()
        return unit_b.scalar_mult(self.dot_product(unit_b))

    def ortho(self, basis):
        return self - self.proj(basis)

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
    #   epsilon: allowable tolerance between the normalized dot product and values
    #       {-1 or 1}
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
        x = Decimal(0.0)
        for e in self.coordinates:
            x += e ** Decimal(2.0)
        return x ** Decimal(0.5)

    def normalize(self):
        try:
            return self.scalar_mult(Decimal(1.0)/self.get_mag())

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
    v1 = Vector([3.039, 1.879])
    b1 = Vector([0.825, 2.036])

    v2 = Vector([-9.88, -3.264, -8.159])
    b2 = Vector([-2.155, -9.353, -9.473])

    v3 = Vector([3.009, -6.172, 3.692, -2.51])
    b3 = Vector([6.404, -9.144, 2.759, 8.718])

    print(round(v1.proj(b1), 3))
    print(round(b2.normalize(), 3))
    print(round(v2.ortho(b2), 3))
    print(round(v3.proj(b3), 3))
    print(round(v3.ortho(b3), 3))


if __name__ == '__main__':
    test()
