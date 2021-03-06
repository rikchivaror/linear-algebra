from decimal import Decimal, getcontext
from vector import Vector

getcontext().prec = 30


class Plane(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension

            initial_index = Plane.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    # -----------------------------------------------------------------------------
    # is_parallel(self, other):
    #   Determine if two planes are parallel. This is true if the normal vectors of
    #   the two planes are parallel. The is_parallel() method of the Vector class is
    #   utilized in this method.
    #
    # Arguments:
    #   self, other: Plane objects
    #
    # Returns:
    #   the 'bool' type based on whether the vectors are parallel
    def is_parallel(self, other):
        return self.normal_vector.is_parallel(other.normal_vector)

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Plane.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def __eq__(self, other):

        if not self.is_parallel(other):
            return False

        try:    # an exception occurs if one of the planes has a zero normal vector
            basepoint_diff = other.basepoint - self.basepoint
        except TypeError:
            if not other.basepoint and not self.basepoint:
                return True
            return False

        return basepoint_diff.is_orthogonal(self.normal_vector)

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


def test():
    n_l_1 = Vector([1, 1, 1])
    k_1 = 1

    n_l_2 = Vector([-3, -3, -3])
    k_2 = -3

    p_1 = Plane(n_l_1, k_1)
    p_2 = Plane(n_l_2, k_2)

    print('Line 1 is parallel to line 2: ')
    print(p_1.is_parallel(p_2))

    print('\nLine 1 is equal to line 2: ')
    print(p_1 == p_2)
    #
    # print('\nIntersection of line 1 and line 2 is: ')
    # print(l_1.get_intersection(l_2))


if __name__ == '__main__':
    test()