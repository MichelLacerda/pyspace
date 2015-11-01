import math


class Vec2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        if hasattr(x, "__getitem__"):
            x, y, = x
            self._v = [float(x), float(y)]
        else:
            self._v = [float(x), float(y)]

    # Para debug, retorna composição do vetor: Vec2(0, 0)
    def __repr__(self):
        return('Vec2({0}, {1})'.format(self.x, self.y))

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = 1.0 * value

    ZERO = (0, 0)

    # rhs: Right Hand Side (lado direito)
    def __add__(self, rhs):
        return Vec2(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vec2(self.x + rhs.x, self.y + rhs.y)

    def __mul__(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vec2(self.x / scalar, self.y * scalar)

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)

    def points(p1, p2):
        return Vec2(p2[0] - p1[0], p2[1] - p1[1])

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        m = self.magnitude()
        try:
            self.x /= m
            self.y /= m
        except ZeroDivisionError:
            self.x = 0
            self.y = 0

if __name__ == "__main__":
    # testes
    A = (10.0, 20.0)
    B = (30.0, 35.0)
    C = (15.0, 45.0)
    AB = Vec2.points(A, B)
    BC = Vec2.points(B, C)

    AC = Vec2.points(A, C)
    print("AC: ", AC)

    AC = AB + BC
    print("AB + AC: ", AC)

    print('Vector AB [20.0, 15.0]:', AB)
    print('Magnetude do Vector é [25.0]:', AB.magnitude())
    AB.normalize()
    print('Vector AB Normalize é [0.8, 0.6]:', AB)
