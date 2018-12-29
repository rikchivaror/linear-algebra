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
    def is_orthogonal(self, other, epsilon=1e-10):
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

    # -----------------------------------------------------------------------------
    # cross_prod(self, other):
    #   Calculate the coordinates of a vector that is the cross-products of the
    #   input vectors 'self' and 'other'.
    #
    # Arguments:
    #   self, other: Vector objects
    #
    # Returns:
    #   A vector which is the cross-product of 'self' and 'other'
    def cross_prod(self, other):
        if not (self.dimension == 2 or self.dimension == 3):
            raise Exception("The rank of one or more vectors violates {dim ϵ (2, 3)}")
        elif self.dimension != other.dimension:
            raise Exception("Both vectors are not of the same rank")

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

    # -----------------------------------------------------------------------------
    # area_parallelogram(self, other):
    #   Determine the area of a parallelogram spanned by the vectors 'self' and other
    #
    # Arguments:
    #   self, other: Vector objects
    #
    # Returns:
    #   An object of the Decimal class which represents the area of a parallelogram
    def area_parallelogram(self, other):
        x_prod = self.cross_prod(other)
        return x_prod.get_mag()

    # -----------------------------------------------------------------------------
    # area_triangle(self, other):
    #   Determine the area of a triangle spanned by the vectors 'self' and other
    #
    # Arguments:
    #   self, other: Vector objects
    #
    # Returns:
    #   An object of the Decimal class which represents the area of a triangle
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
        num_decimal_places = 3
        self.coordinates = tuple(round(float(x), num_decimal_places) for x in self.coordinates)
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

    def __getitem__(self, i):
        return self.coordinates[i]

    def __iter__(self):
        return self.coordinates.__iter__()


def test():
    v = Vector([5, 3])
    w = Vector([-1, 0, 6])

    print(round(v.cross_prod(w), 3))


if __name__ == '__main__':
    test()
