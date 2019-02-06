from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane     #TODO: generalize this class to higher dimensions by creating a hyperplane class (lesson 3, part 25)

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    # -----------------------------------------------------------------------------
    # solve_system(self):
    #   Extract a system solution from its reduced row-echelon form following Gaussian
    #   Elimination (GE) procedure. There are three types of cases for the solution
    #   to a system of equations.
    #      - unique solution: each variable is a pivot variable
    #      - no solution: the system is inconsistent, which means we find 0 = k where
    #           k is non-zero following Gaussian elimination
    #      - infinite solution set: there are one or more free variables in the system
    #           of equations following GE. Note, the number of free variables indicates
    #           the dimension of the solution set.
    #
    # Arguments:
    #   self: a LinearSystem object
    #
    # Returns:
    #   solution: - a Vector object (for unique solution)
    #             - String object (if no solution exists or infinitely many solutions)
    def solve_system(self):
        system = self.compute_rref()
        fnzt_indices = system.indices_of_first_nonzero_terms_in_each_row()[:self.dimension]

        for row_i, pivot_i in enumerate(fnzt_indices):               # if FNZT for any row is -1 (all terms 0) and where
            if pivot_i == -1 and system[row_i].constant_term != 0:   # constant term k is non-zero, the system has no
                return system.NO_SOLUTIONS_MSG                       # solution

        return system.make_parametric()

    # -----------------------------------------------------------------------------
    # make_parametric(self):
    #   Helper function for solve_system(self) which outputs the parametrization
    #   of the solution set.
    #
    # Arguments:
    #   self: a LinearSystem object
    #
    # Returns:
    #   solution: - a Parametrization object for the case where we have a unique
    #               or infinite solution set
    #             - String object (if no solution exists or infinitely many solutions)
    def make_parametric(self):
        base_point = []
        dir_vectors = []
        fnzt_indices = self.indices_of_first_nonzero_terms_in_each_row()[:self.dimension]

        for row_i, pivot_i in enumerate(fnzt_indices):
            base_point.append(self[row_i].constant_term)

            if pivot_i == -1:
                dir_vectors.append([0] * self.dimension)

                for row_j in range(self.dimension):
                    if self[row_j].normal_vector[row_i]:
                        dir_vectors[-1][row_j] = self[row_j].normal_vector[row_i]

                dir_vectors[-1][row_i] = 1
                dir_vectors[-1] = Vector(dir_vectors[-1])

        return Parametrization(Vector(base_point), dir_vectors)

    # -----------------------------------------------------------------------------
    # compute_rref(self):
    #   Bring the system of equations into reduced row echelon form.
    #                  --                  --
    #                  | 1  0  0      0 = x |
    #                  | 0  1  0  ... 0 = x |
    #   LinearSystem = | 0  0  1      0 = x |
    #                  |    :         :     |
    #                  | 0  0  0  ... 1 = x |
    #                  --                  --
    # Arguments:
    #   self: a LinearSystem object
    #
    # Returns:
    #   LinearSystem object
    def compute_rref(self):
        tf = self.compute_triangular_form()
        fnzt_indices = tf.indices_of_first_nonzero_terms_in_each_row()

        for row_i, pivot_i in enumerate(fnzt_indices):      # 'row_i' indexes each row in the system of eq. referenced
            pivot_term = tf[row_i].normal_vector[pivot_i]   # by 'tf' for which row-reduction will be performed

            if not (pivot_term == 1 or pivot_i == -1):
                tf.multiply_coefficient_and_row(1/pivot_term, row_i)

            for term_i in range(tf.dimension):              # cycle through each non-zero term in 'row_i' and perform
                term = tf[row_i].normal_vector[term_i]      # row-reduction on terms that have an index greater than

                if not (term and term_i > pivot_i):         # the pivot term
                    continue

                try:
                    row_j = fnzt_indices.index(term_i)      # 'row_j' is the index of the first row below 'row_i'

                except ValueError:                          # that has a pivot term at the same index as 'term_i'
                    continue

                beta = - term / tf[row_j].normal_vector[term_i]         # do row-reduction on target row: 'row_i'
                tf.add_multiple_times_row_to_row(beta, row_j, row_i)    # using 'row_j'

        return tf

    # -----------------------------------------------------------------------------
    # compute_triangular_form(self):
    #   Bring the system of equations into triangular form. This is a helper function
    #   for compute_rref(self).
    #                  --                  --
    #                  | x  x  x      x = x |
    #                  | 0  x  x  ... x = x |
    #   LinearSystem = | 0  0  x      x = x |
    #                  |    :         :     |
    #                  | 0  0  0  ... x = x |
    #                  --                  --
    # Arguments:
    #   self: a LinearSystem object
    #
    # Returns:
    #   LinearSystem object
    # TODO: re-factor this method so it's easier to read
    def compute_triangular_form(self):
        system = deepcopy(self)
        rank = len(system)

        for row_i in range(rank-1):
            fnzt_indices = system.indices_of_first_nonzero_terms_in_each_row()  # find next row below row_i with the
            lower_row_fnzt_indices = fnzt_indices[row_i+1:]                     # lowest index containing first non-zero
            smallest_fnzt_index = min(lower_row_fnzt_indices)                   # term (FNZT)

            if smallest_fnzt_index < fnzt_indices[row_i]:       # swap row_i with a row that has the smallest FNZT index
                row_to_swap = lower_row_fnzt_indices.index(smallest_fnzt_index) + row_i + 1
                system.swap_rows(row_i, row_to_swap)

            for row_j in range(row_i+1, rank):
                fnzt_indices = system.indices_of_first_nonzero_terms_in_each_row()  # update the FNZT indices

                if fnzt_indices[row_i] == fnzt_indices[row_j]:                      # if the FNZT index of the row_j
                    numerator = system[row_j].normal_vector[fnzt_indices[row_j]]    # matches the FNZT index of the
                    denominator = system[row_i].normal_vector[fnzt_indices[row_i]]  # current row then multiply coef.
                    beta = - numerator / denominator                                # with row_i, add that to row_j and
                    system.add_multiple_times_row_to_row(beta, row_i, row_j)        # replace row_j with result

        return system

    # -----------------------------------------------------------------------------
    # swap_rows(self, row1, row2):
    #   Swap the position of two Plane objects within the LineaSystem object list
    #
    # Arguments:
    #   self: a LinearSystem object
    #   row1, row2: index of the list of Plane objects within the LinearSystem object
    #
    # Returns:
    #   None
    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]

    # -----------------------------------------------------------------------------
    # multiply_coefficient_and_row(self, coefficient, row):
    #   For a given Plane within the LinearSystem multiply its normal vector and
    #   constant term with the coefficient.
    #
    # Arguments:
    #   self: a LinearSystem object
    #   row: Integer which indexes a Plane object within the LinearSystem object
    #   coefficient: Integer type
    #
    # Returns:
    #   None
    def multiply_coefficient_and_row(self, coefficient, row):
        normal_vector = self[row].normal_vector.scalar_mult(coefficient)
        coefficient = coefficient * self[row].constant_term
        self[row] = Plane(normal_vector, coefficient)

    # -----------------------------------------------------------------------------
    # add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
    #   For a given Plane multiply both sides of the equation with the coefficient
    #   and add each side of the equation to each size of an equation for another
    #   Plane. Only the attributes of the Plane indexed by 'row_to_be_added' are modified.
    #
    # Arguments:
    #   self: a LinearSystem object
    #   row_to_add, row_to_be_added_to: Integer which indexes a Plane object within
    #   the LinearSystem object
    #   coefficient: Integer type
    #
    # Returns:
    #   None
    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        normal_vector = self[row_to_add].normal_vector.scalar_mult(coefficient) + \
                        self[row_to_be_added_to].normal_vector
        constant_term = coefficient * self[row_to_add].constant_term + self[row_to_be_added_to].constant_term
        self[row_to_be_added_to] = Plane(normal_vector, constant_term)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i, p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, i):
        return self.planes[i]

    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


class Parametrization(object):

    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM = (
        'The basepoint and direction vectors should all live in the same '
        'dimension')

    def __init__(self, basepoint, direction_vectors):

        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension

        except AssertionError:
            raise Exception(self.BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM)

    def __str__(self):

        output = ''
        for coord in range(self.dimension):
            output += 'x_{} = {}'.format(coord + 1,
                                          round(self.basepoint[coord], 3))
            for free_var, vector in enumerate(self.direction_vectors):
                output += ' + {} t_{}'.format(round(vector[coord], 3),
                                             free_var + 1)
            output += '\n'
        return output


def test():
    p1 = Plane(normal_vector=Vector(['5.862', '1.178', '-10.366']), constant_term='-8.15')
    p2 = Plane(normal_vector=Vector(['-2.931', '-0.589', '5.183']), constant_term='-4.075')
    s = LinearSystem([p1, p2])
    print(s.solve_system())

    p1 = Plane(normal_vector=Vector(['8.631', '5.112', '-1.816']), constant_term='-5.113')
    p2 = Plane(normal_vector=Vector(['4.315', '11.132', '-5.27']), constant_term='-6.775')
    p3 = Plane(normal_vector=Vector(['-2.158', '3.01', '-1.727']), constant_term='-0.831')
    s = LinearSystem([p1, p2, p3])
    print(s.solve_system())

    p1 = Plane(normal_vector=Vector(['5.262', '2.739', '-9.878']), constant_term='-3.441')
    p2 = Plane(normal_vector=Vector(['5.111', '6.358', '7.638']), constant_term='-2.152')
    p3 = Plane(normal_vector=Vector(['2.016', '-9.924', '-1.376']), constant_term='-9.278')
    p4 = Plane(normal_vector=Vector(['2.167', '-13.593', '-18.883']), constant_term='-10.567')
    s = LinearSystem([p1, p2, p3, p4])
    print(s.solve_system())

    p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
    p3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
    p4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
    s = LinearSystem([p1, p2, p3, p4])
    print(s.solve_system())

    p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
    s = LinearSystem([p1,p2])
    print(s.solve_system())

    p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
    p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
    s = LinearSystem([p1,p2,p3])
    print(s.solve_system())

    p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
    s = LinearSystem([p1, p2])
    print(s.solve_system())
    #
    # print(s.indices_of_first_nonzero_terms_in_each_row())
    # print('{},{},{},{}'.format(s[0],s[1],s[2],s[3]))
    # print(len(s))
    # print(s)
    #
    # s[0] = p1
    # print(s)
    #
    # print(MyDecimal('1e-9').is_near_zero())
    # print(MyDecimal('1e-11').is_near_zero())


if __name__ == '__main__':
    test()
