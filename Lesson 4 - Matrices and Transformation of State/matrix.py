from vector import Vector


class Matrix(object):

    ALL_VECTORS_MUST_BE_IN_SAME_DIM_MSG = 'All rows should have the same dimension'
    MATRICES_MUST_BE_THE_SAME_SIZE_MSG = 'Both matrices must have the same dimension'
    NUMBER_OF_A_COLS_AND_B_ROWS_DIFFERENT_MSG = 'Number of columns in A not equal to number of columns in matrix B'

    def __init__(self, M):

        try:
            d = len(M[0])
            for v in M:
                assert len(v) == d

            self.matrix = M
            self.n_dim = d
            self.m_dim = len(M)

        except AssertionError:
            raise Exception(self.ALL_VECTORS_MUST_BE_IN_SAME_DIM_MSG)

    def get_column(self, k):
        column = []

        for i in range(self.m_dim):
            column.append(self.matrix[i][k])

        return column

    def transpose(self):
        transp_M = []

        for i in range(self.n_dim):
            transp_M.append(self.get_column(i))

        return Matrix(transp_M)

    def matrix_mult(self, M):
        new_M = []

        try:
            assert self.n_dim == M.m_dim        # check that that n-dimension of 'self' is equal to m-dimension of 'M'

        except AssertionError:
            raise Exception(self.NUMBER_OF_A_COLS_AND_B_ROWS_DIFFERENT_MSG)

        for i in range(self.m_dim):             # for each row in 'self' matrix put that row into a vector object
            row_vector = Vector(self.matrix[i])
            new_M.append([])
                                                                        # for each column in the 'M' matrix
            for j in range(M.n_dim):                                    # put that column into a vector object
                col_vector = Vector(M.get_column(j))                    # compute the dot product of the two vectors
                new_M[i].append(row_vector.dot_product(col_vector))     # place the result into a new matrix at the same
                                                                        # row as the vector from the 'self' matrix
        return Matrix(new_M)                                            # and the same column as the 'M' matrix

    def scalar_mult(self, c):
        scaled_M = []

        for i in range(self.m_dim):
            scaled_M.append([])
            for j in range(self.n_dim):
                scaled_M[i].append(c * self.matrix[i][j])

        return Matrix(scaled_M)

    def matrix_addition(self, M):
        matrix_sum = []
        row = []

        try:
            assert self.n_dim == M.n_dim and self.m_dim == M.m_dim

        except AssertionError:
            raise Exception(self.MATRICES_MUST_BE_THE_SAME_SIZE_MSG)

        for i in range(self.m_dim):
            for j in range(self.n_dim):
                row.append(self.matrix[i][j] + M.matrix[i][j])
            matrix_sum.append(row)
            row = []

        return Matrix(matrix_sum)

    def test_same_size(self, M):
        try:
            assert self.n_dim == M.n_dim and self.m_dim == M.m_dim

        except AssertionError:
            raise Exception(self.MATRICES_MUST_BE_THE_SAME_SIZE_MSG)

    def __eq__(self, M):
        if not self.n_dim == M.n_dim and self.m_dim == M.m_dim:
            return False

        for i in range(self.m_dim):
            if self.matrix[i] != M.matrix[i]:
                return False

        return True

    def __str__(self):
        precision = 2
        ret = 'Matrix:\n'
        max_col_length = [0] * self.n_dim

        for i in range(self.m_dim):                         # determine space requirements for each matrix column
            for j, e in enumerate(self.matrix[i]):
                int_length = str(float(e)).index('.')
                col_length = int_length + precision + 3     # constant '3' takes into account two empty spaces to the
                if col_length > max_col_length[j]:          # left of the number and the space occupied by the decimal
                    max_col_length[j] = col_length

        for i in range(self.m_dim):                         # print the matrix and format each element so that all
            ret += '['                                      # elements in a column are right justified with each other
            for j, e in enumerate(self.matrix[i]):
                ret += '{0:{width}.{prec}f}'.format(e, width=max_col_length[j], prec=precision)
            ret += '  ]\n'

        return ret


def test():
    A = Matrix([[17, 25, 6, 2],
                [6, 1, 97, 4],
                [80, 8, 54, 15]
                ])

    B = Matrix([[3, 14, 1, 7, 42, 5],
                [32, 11, 2, 4, 18, 17],
                [19, 81, 4, 8, 5, 10],
                [27, 2, 3, 6, 7, 3]
                ])

    print(A.matrix_mult(B))


if __name__ == '__main__':
    test()
