import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component found'

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
    # projection_to(self, basis):
    #   Determine the parallel component of the vector passed into 'self' with the
    #   'basis' vector. To calculate this we use the formula:
    #   (self_vec ‖ basis_vec) = basis_unit_vec * ( self_vec • u_basis_vec )
    #
    # Arguments:
    #   self: any Vector object
    #   basis: the basis Vector that the parallel component of 'self' will be determined from.
    #
    # Returns:
    #   the Vector component of 'self' that is parallel to 'bas'is.
    def projection_to(self, basis):
        try:
            unit_b = basis.normalize()
            return unit_b.scalar_mult(self.dot_product(unit_b))

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('No unique parallel component found')
            else:
                raise e

    # -----------------------------------------------------------------------------
    # orthogonal_to(self, basis):
    #   Determine the orthogonal component of the vector 'self' with the 'basis'
    #   vector. To calculate this we use the formula:
    #   (self_vec ┴ basis_vec) = self_vec - ( self_vec • u_basis_vec )
    #
    # Arguments:
    #   self: any Vector object
    #   basis: the basis Vector that the orthogonal component of 'self' will be determined by.
    #
    # Returns:
    #   the Vector component of 'self' that is orthogonal to 'basis'.
    def orthogonal_to(self, basis):
        try:
            return self - self.projection_to(basis)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

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

    def cross_prod(self, other):
        # TODO: throw an exception if either vector passed into the function have a rank other than 2 or 3 and both vectors are not the same rank
        # TODO: if vectors passed in are BOTH dim = 2, then extend the vectors into three dimensions with z-coord = 0

        x_prod = [0, 0, 0]
        v = list(self.coordinates)
        w = list(other.coordinates)

        if self.dimension == 2:
            v.append(Decimal(0.0))
            w.append(Decimal(0.0))

        x_prod[0] = v[1] * w[2] - w[1] * v[2]
        x_prod[1] = w[0] * v[2] - v[0] * w[2]
        x_prod[2] = v[0] * w[1] - w[0] * v[1]

        return Vector(x_prod)

    def area_parallelogram(self, other):
        x_prod = self.cross_prod(other)
        return x_prod.get_mag()

    def area_triangle(self, other):
        return self.area_parallelogram(other) / Decimal(2.0)

    def dot_product(self, other):
        y = 0
        for i in range(self.dimension):
            y += self.coordinates[i] * other.coordinates[i]
        return y

    def get_angle(self, other):
        try:
            u1 = self.normalize()
            u2 = other.normalize()

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception("Cannot compute an angle with the zero vector")
            else:
                raise e

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
        # TODO: print vectors without the 'Decimal' prefix prior to each co-ordinate.
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, other):
        result = []
        for i in range(self.dimension):
            result.append(self.coordinates[i] + other.coordinates[i])
        return Vector(result)

    def __sub__(self, other):
        result = []
        for i in range(self.dimension):
            result.append(self.coordinates[i] - other.coordinates[i])
        return Vector(result)

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
    # v1 = Vector([3.039, 1.879])
    # b1 = Vector([0.825, 2.036])
    #
    # v2 = Vector([-9.88, -3.264, -8.159])
    # b2 = Vector([-2.155, -9.353, -9.473])
    #
    # v3 = Vector([3.009, -6.172, 3.692, -2.51])
    # b3 = Vector([6.404, -9.144, 2.759, 8.718])

    v = Vector([5, 3])
    w = Vector([-1, 0])

    print(round(v.cross_prod(w), 3))

    # print(round(v1.get_angle(b4)))
    # print(round(b4.normalize()))
    # print(round(v1.proj(b1), 3))
    # print(round(b2.normalize(), 3))
    # print(round(v2.ortho(b2), 3))
    # print(round(v3.proj(b3), 3))
    # print(round(v3.ortho(b3), 3))


if __name__ == '__main__':
    test()
