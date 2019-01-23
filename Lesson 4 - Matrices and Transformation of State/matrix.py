from vector import Vector
from decimal import Decimal, getcontext

getcontext().prec = 30


class Matrix(object):

    ALL_VECTORS_MUST_BE_IN_SAME_DIM_MSG = 'All rows should have the same dimension'

    def __init__(self, vectors):

        try:
            d = vectors[0].dimension
            for v in vectors:
                assert v.dimension == d

            self.vectors = vectors
            self.row_dimension = d
            self.col_dimension = len(vectors)

        except AssertionError:
            raise Exception(self.ALL_VECTORS_MUST_BE_IN_SAME_DIM_MSG)

    def scalar_mult(self, c):
        pass

    def __str__(self):
        precision = 2
        ret = 'Matrix:\n'
        max_length = 0

        for i in range(self.col_dimension):
            for e in self.vectors[i]:
                length = len(str(int(e)))
                if length > max_length:
                    max_length = length

        for i in range(self.col_dimension):
            for e in self.vectors[i]:
                ret += '{0:{width}.{prec}f}'.format(e, width=max_length+precision+3, prec=precision)
            ret += '\n'

        return ret


def test():
    v1 = Vector([1.5236, -.354, 3])
    v2 = Vector([4, 5, 6])

    M = Matrix([v1, v2])

    print(M)


if __name__ == '__main__':
    test()
