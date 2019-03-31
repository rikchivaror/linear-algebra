from decimal import Decimal, getcontext
from vector import Vector
from copy import deepcopy

getcontext().prec = 30


class Matrix(object):

    ALL_VECTORS_MUST_BE_IN_SAME_DIM_MSG = 'All rows should have the same dimension'
    MATRICES_MUST_BE_THE_SAME_SIZE_MSG = 'Both matrices must have the same dimension'
    NUMBER_OF_A_COLS_AND_B_ROWS_DIFFERENT_MSG = 'Number of columns in A not equal to number of columns in matrix B'
    MATRIX_MUST_BE_SQUARE = 'The matrix must be square to perform the operation'
    MATRIX_NOT_INVERTIBLE = 'The matrix is not invertible since det(A) = 0'
    ALL_ROWS_MUST_BE_IN_SAME_DIM_MSG = 'All rows should have the same length'

    def __init__(self, M=None, size=0):
        self.square = False
        self.is_ref = False

        if type(M) == list:
            d = len(M[0])

            try:
                for v in M:
                    assert len(v) == d

            except AssertionError:
                raise Exception(self.ALL_VECTORS_MUST_BE_IN_SAME_DIM_MSG)

            self.matrix = M
            self.n_dim = d
            self.m_dim = len(M)
            if self.n_dim == self.m_dim:
                self.square = True
        else:
            self.matrix = []
            self.n_dim, self.m_dim = [size] * 2
            self.square = True

            for i in range(size):
                self.matrix.append([])

                for j in range(size):
                    if M == 'I':
                        if i == j:
                            element = 1
                        else:
                            element = 0
                    else:
                        element = M

                    self[i].append(element)

    def get_inverse(self):
        self.is_square()
        det, ref_M, right_side_M = self.get_determinant(Matrix('I', self.n_dim))

        try:
            assert det != 0

        except AssertionError:
            Exception(self.MATRIX_NOT_INVERTIBLE)

        return ref_M.get_rref(right_side_M)[1]

    def get_determinant(self, right_side_M=None):
        self.is_square()
        det = 1
        ref_M, right_side_M = self.get_ref(right_side_M)

        for i in range(self.m_dim):
            det *= ref_M[i, i]

        return det, ref_M, right_side_M

    def get_ref(self, right_side_M):
        left_side_M = deepcopy(self)

        for i in range(left_side_M.m_dim-1):
            pivot_indices = left_side_M.get_row_pivot()         # find next row below row_i with the lowest
            sub_pivot_indices = pivot_indices[i+1:]             # index containing the first pivot term
            smallest_pivot_i = min(sub_pivot_indices)

            if smallest_pivot_i < pivot_indices[i]:             # swap row i with row that has the smallest pivot index
                row_to_swap = sub_pivot_indices.index(smallest_pivot_i) + i + 1
                left_side_M.swap_rows(i, row_to_swap)

                if right_side_M:
                    right_side_M.swap_rows(i, row_to_swap)

            for j in range(i+1, left_side_M.m_dim):
                pivot_indices = left_side_M.get_row_pivot()     # update the pivot indices of each row in matrix

                if pivot_indices[i] == pivot_indices[j]:                    # if the FNZT index of the row_j
                    numerator = left_side_M.matrix[j][pivot_indices[j]]     # matches the FNZT index of the
                    denominator = left_side_M.matrix[i][pivot_indices[i]]   # current row then multiply coefficient
                    beta = (-1) * numerator / denominator                   # with row_i, add that to row_j and
                    left_side_M.add_scaled_row_to_row(beta, i, j)           # replace row_j with result

                    if right_side_M:
                        right_side_M.add_scaled_row_to_row(beta, i, j)

        left_side_M.is_ref = True
        return left_side_M, right_side_M

    def get_rref(self, right_side_M):         # TODO: implement this method
        if not self.is_ref:
            left_side_M, right_side_M = self.get_ref(right_side_M)
        else:
            left_side_M = deepcopy(self)

        pivot_indices = left_side_M.get_row_pivot()

        for row_i, pivot_i in enumerate(pivot_indices):      # 'row_i' indexes each row in the system of eq. referenced
            pivot_term = left_side_M.matrix[row_i][pivot_i]   # by 'tf' for which row-reduction will be performed

            if not (pivot_term == 1 or pivot_i == -1):
                left_side_M.scale_row(1/pivot_term, row_i)
                right_side_M.scale_row(1/pivot_term, row_i)

            for term_i in range(left_side_M.m_dim):              # cycle through each non-zero term in 'row_i' and perform
                term = left_side_M.matrix[row_i][term_i]      # row-reduction on terms that have an index greater than

                if not (term and term_i > pivot_i):         # the pivot term
                    continue

                try:
                    row_j = pivot_indices.index(term_i)      # 'row_j' is the index of the first row below 'row_i'

                except ValueError:                          # that has a pivot term at the same index as 'term_i'
                    continue

                beta = (-1) * term / left_side_M.matrix[row_j][term_i]         # do row-reduction on target row: 'row_i'
                left_side_M.add_scaled_row_to_row(beta, row_j, row_i)    # using 'row_j'
                right_side_M.add_scaled_row_to_row(beta, row_j, row_i)

        return left_side_M, right_side_M

    def swap_rows(self, row_i, row_j):
        self[row_i], self[row_j] = self[row_j], self[row_i]

    def scale_row(self, factor, row_i):
        scaled_row = Matrix([self[row_i]]).scalar_mult(factor)
        self[row_i] = scaled_row[0]

    def add_scaled_row_to_row(self, factor, row_s, row_t):
        new_row = Vector(self[row_s]).scalar_mult(factor) + Vector(self[row_t])
        self[row_t] = list(new_row.coordinates)

    def get_row_pivot(self):
        num_rows = self.m_dim
        indices = [-1] * num_rows

        for i, row in enumerate(self.matrix):
            for j, e in enumerate(row):
                if not MyDecimal(e).is_near_zero():
                    indices[i] = j
                    break

        return indices

    def is_square(self):
        try:
            assert self.square

        except AssertionError:
            raise Exception(self.MATRIX_MUST_BE_SQUARE)

    def get_column(self, k):
        column = []

        for i in range(self.m_dim):
            column.append(self[i, k])

        return column

    def transpose(self):
        transp_M = []

        for i in range(self.n_dim):
            transp_M.append(self.get_column(i))

        return Matrix(transp_M)

    def matrix_mult(self, M):
        try:
            assert self.n_dim == M.m_dim        # check that that n-dimension of 'self' is equal to m-dimension of 'M'

        except AssertionError:
            raise Exception(self.NUMBER_OF_A_COLS_AND_B_ROWS_DIFFERENT_MSG)

        new_M = []
        M_t = M.transpose()

        for i in range(self.m_dim):             # for each row in 'self' matrix put that row into a vector object
            row_1 = Vector(self[i])
            new_M.append([])

            for j in range(M.n_dim):                        # multiply each row of the 'self' matrix with each row of
                row_2 = Vector(M_t[j])               # the transposed 'M' matrix
                new_M[i].append(row_1.dot_product(row_2))   # place the result into position i,j of the new matrix

        return Matrix(new_M)

    def scalar_mult(self, c):
        scaled_M = []

        for i in range(self.m_dim):
            scaled_M.append([])

            for j in range(self.n_dim):
                scaled_M[i].append(c * self[i, j])

        return Matrix(scaled_M)

    def matrix_addition(self, M):
        self.test_same_size(M)
        matrix_sum = []
        row = []

        for i in range(self.m_dim):
            for j in range(self.n_dim):
                row.append(self[i, j] + M[i, j])

            matrix_sum.append(row)
            row = []

        return Matrix(matrix_sum)

    def test_same_size(self, M):
        try:
            assert (self.n_dim, self.m_dim) == (M.n_dim, M.m_dim)

        except AssertionError:
            raise Exception(self.MATRICES_MUST_BE_THE_SAME_SIZE_MSG)

    def __eq__(self, M):
        if not self.n_dim == M.n_dim and self.m_dim == M.m_dim:
            return False

        for i in range(self.m_dim):
            if self[i] != M[i]:
                return False

        return True

    def __str__(self):
        precision = 2
        ret = 'Matrix:\n'
        max_col_length = [0] * self.n_dim

        for i in range(self.m_dim):                         # determine space requirements for each matrix column
            for j, e in enumerate(self[i]):
                int_length = str(float(e)).index('.')
                col_length = int_length + precision + 3     # constant '3' takes into account two empty spaces to the
                if col_length > max_col_length[j]:          # left of the number and the space occupied by the decimal
                    max_col_length[j] = col_length

        for i in range(self.m_dim):                         # print the matrix and format each element so that all
            ret += '['                                      # elements in a column are right justified with each other
            for j, e in enumerate(self[i]):
                ret += '{0:{width}.{prec}f}'.format(e, width=max_col_length[j], prec=precision)
            ret += '  ]\n'

        return ret

    def __getitem__(self, pos):
        if type(pos) == tuple:
            i, j = pos
            return self.matrix[i][j]
        else:
            return self.matrix[pos]

    def __setitem__(self, i, x):
        try:
            assert self.n_dim == len(x)
            self.matrix[i] = x

        except AssertionError:
            raise Exception(self.ALL_ROWS_MUST_BE_IN_SAME_DIM_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


def test():

    # # test get_row_pivot()
    # A = Matrix([[1, 4, 3, 2],
    #             [0, 2, 1, 2],
    #             [0, 0, 2, 3],
    #             [0, 2, 2, 3],
    #             [0, 0, 0, 0]])
    #
    #
    # print(A.get_row_pivot())
    # print()
    #
    # # test __setitem__()
    # A[2] = [3, 3, 3, 3]
    # print(A)
    #
    # # test __getitem__()
    # print(A[2, 2])
    #
    # # test swap_rows()
    # A.swap_rows(2, 4)
    # print(A)
    #
    # # test scale_row()
    # A.scale_row(3, 1)
    # print(A)
    #
    # # test add_scaled_row_to_row()
    # A.add_scaled_row_to_row(2, 0, 2)
    # print(A)
    #
    # # test get_ref(), test case 1
    # A = Matrix([[0, 1, 1],
    #             [1, -1, 1],
    #             [1, 2, -5]
    #             ])
    #
    # B = Matrix([[1],
    #             [2],
    #             [3]
    #             ])
    #
    # A, B = A.get_ref(B)
    # print(A)
    # print(B)
    #
    # # test get_ref(), test case 2
    # A = Matrix([[1, 1, 1],
    #             [0, 1, 0],
    #             [1, 1, -1],
    #             [1, 0, -2]
    #             ])
    #
    # B = Matrix([[1],
    #             [2],
    #             [3],
    #             [2]
    #             ])
    #
    # A, B = A.get_ref(B)
    # print(A)
    # print(B)
    #
    # # test get_ref(), test case 3
    # A = Matrix([[1, 6, 5],
    #             [3, 1, 1],
    #             [2, 1, 2],
    #             ])
    #
    # B = Matrix('I', 3)
    #
    # A, B = A.get_ref(B)
    # print(A)
    # print(B)
    #
    # # test get_determinant(), test case 1
    # A = Matrix([[1, 6, 5],
    #             [3, 1, 1],
    #             [2, 1, 2],
    #             ])
    #
    # B = Matrix('I', 3)
    #
    # det, A, B = A.get_determinant(B)
    # print(det)
    # print(A)
    # print(B)

    # test get_determinant(), test case 2
    A = Matrix([[1, 6, 5],
                [3, 1, 1],
                [2, 1, 2],
                ])

    det, A, B = A.get_determinant()
    print(det)
    print(A)
    print(B)


    # test get_inverse(), test case 2
    A = Matrix([[1, 6, 5],
                [3, 1, 1],
                [2, 1, 2],
                ])
    print(A.get_inverse())

if __name__ == '__main__':
    test()

