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
        u1 = self.normalize()
        u2 = other.normalize()
        return math.acos(u1.dot_product(u2))

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

    def normalize(self):
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
    v1 = Vector([1, 2, -1])
    v2 = Vector([3, 1, 0])
    v3 = Vector([-7.579, -7.88])
    v4 = Vector([22.64, 23.64])
    v5 = Vector([-2.029, 9.97, 4.172])
    v6 = Vector([-9.231, -6.639, -7.245])
    v7 = Vector([-2.328, -7.284, -1.214])
    v8 = Vector([-1.821, 1.072, -2.94])


    # test for Vector.dot_product() method
    print(v3.dot_product(v4))
    print(v5.dot_product(v6))
    print(v7.dot_product(v8))

    # test for Vector.get_angle() method
    # print(math.degrees((v1.get_angle(v2))))
    print(math.degrees((v3.get_angle(v4))))
    print(math.degrees((v5.get_angle(v6))))
    print(math.degrees((v7.get_angle(v8))))

if __name__ == '__main__':
    test()
