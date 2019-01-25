# from vector import Vector


class Matrix(object):

    ALL_VECTORS_MUST_BE_IN_SAME_DIM_MSG = 'All rows should have the same dimension'

    def __init__(self, matrix):

        try:
            d = len(matrix[0])
            for v in matrix:
                assert len(v) == d

            self.matrix = matrix
            self.row_dimension = d
            self.col_dimension = len(matrix)

        except AssertionError:
            raise Exception(self.ALL_VECTORS_MUST_BE_IN_SAME_DIM_MSG)

    def scalar_mult(self, c):
        scaled = []

        for i in range(self.col_dimension):
            scaled.append([])
            for j in range(self.row_dimension):
                scaled[i].append(c * self.matrix[i][j])

        return Matrix(scaled)

    def __str__(self):
        precision = 2
        ret = 'Matrix:\n'
        max_col_length = [0] * self.row_dimension

        for i in range(self.col_dimension):
            for j, e in enumerate(self.matrix[i]):
                int_length = str(float(e)).index('.')
                col_length = int_length + precision + 3     # constant '3' takes into account two empty spaces to the
                if col_length > max_col_length[j]:          # left of the number and the space occupied by the decimal
                    max_col_length[j] = col_length

        for i in range(self.col_dimension):
            for j, e in enumerate(self.matrix[i]):
                ret += '{0:{width}.{prec}f}'.format(e, width=max_col_length[j], prec=precision)
            ret += '\n'

        return ret


def test():
    v1 = [-0.56, -1234.354, 3]
    v2 = [1.5236, 5, 6]

    M = Matrix([v1, v2])

    print(M)

    Z = M.scalar_mult(3)
    print(Z)


if __name__ == '__main__':
    test()
