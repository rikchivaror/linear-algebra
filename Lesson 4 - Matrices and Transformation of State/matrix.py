from vector import Vector


class Matrix(object):

    ALL_VECTORS_MUST_BE_IN_SAME_DIM_MSG = 'All rows should have the same dimension'
    MATRICES_MUST_BE_THE_SAME_SIZE_MSG = 'Both matrices must have the same dimension'
    NUMBER_OF_A_COLS_AND_B_ROWS_DIFFERENT_MSG = 'Number of columns in A not equal to number of columns in matrix B'
    MATRIX_MUST_BE_SQUARE = 'The matrix must be square to perform the operation'
    MATRIX_NOT_INVERTIBLE = 'The matrix is not invertible since det(A) = 0'

    def __init__(self, M=None, size=0):
        self.square = False

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
        det = 0
        ref_M, right_side_M = self.get_ref(right_side_M)

        for i in range(self.m_dim):
            det += ref_M[i, i]

        return det, ref_M, right_side_M

    def get_ref(self, right_side_M):       # TODO: implement this method
        # return 'self' and 'right_side_M'
        pass

    def get_rref(self, ANS):         # TODO: implement this method
        # return 'self' and 'ANS'
        pass

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

def test():

    A = Matrix(5, 5)
    B = Matrix(5, 5)

    print(A.test_same_size(B))
    print(A[3, 3])

if __name__ == '__main__':
    test()
