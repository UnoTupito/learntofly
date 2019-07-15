from math import sqrt

class triangle:
    def __init__(self, pointA, pointB, pointC):
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
        ab = sqrt((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2)
        bc = sqrt((pointC[0] - pointB[0]) ** 2 + (pointC[1] - pointB[1]) ** 2)
        ca = sqrt((pointA[0] - pointC[0]) ** 2 + (pointA[1] - pointC[1]) ** 2)
        p = (ab + bc + ca) / 2

    def perimeter(self):
        prmtr = self.ab + self.bc + self.ca
        print(f'периметр треугольника равен {prmtr}')

    def square(self):
        trsquare = sqrt(self.p * (self.p - self.ab) * (self.p - self.bc) * (self.p - self.ca))
        print(f'площадь равна {trsquare}')

    def hight(self):
        h = (2 * sqrt(self.p * (self.p - self.ab) * (self.p - self.bc) * (self.p - self.ca))) / 2
        print(f'высота треугольника равна {h}')


triangle1 = triangle((2, 1), (1, -2), (-1, 0))

triangle1.hight()
triangle1.perimeter()
triangle1.square()
