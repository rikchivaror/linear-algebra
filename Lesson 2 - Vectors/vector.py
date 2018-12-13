import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def dot_product(self, other):
        y = 0
        for i in range(self.dimension):
            y += self.coordinates[i] * other.coordinates[i]
        return y

    def get_angle(self, other):
        dot_product = self.dot_product(other)
        mag_1 = self.get_mag()
        mag_2 = other.get_mag()

        try:
            return math.acos(dot_product / (mag_1 * mag_2))

        except ZeroDivisionError:
            raise Exception("Cannot compute an angle with the zero vector")

    def scalar_mult(self, c):
        x = []
        for e in self.coordinates:
            x.append(c * e)
        return Vector(x)

    def get_mag(self):
        x = 0
        for e in self.coordinates:
            x += e ** 2
        return x ** 0.5

    def get_unit_vec(self):
        try:
            return self.scalar_mult(1/self.get_mag())

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
    vector_1 = Vector([1, 2, -1])
    vector_2 = Vector([3, 1, 0])
    vector_3 = vector_2.scalar_mult(math.pi)
    vector_4 = Vector([0, 0, 0])

    # test for Vector.dot_product() method
    print(vector_1.dot_product(vector_2))

    # test for Vector.get_angle() method
    print((vector_1.get_angle(vector_2)))
    print((vector_2.get_angle(vector_3)))
    print((vector_1.get_angle(vector_4)))


if __name__ == '__main__':
    test()
