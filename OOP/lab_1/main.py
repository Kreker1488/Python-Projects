from math import radians, cos, sin

class Point2D:
    total_points_count = 0
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        Point2D.total_points_count += 1

    def __str__(self):
        return f'({round(self.x, 2)}, {round(self.y, 2)})'

    def __repr__(self):
        return f'Point2D(x={round(self.x, 2)}, y={round(self.y, 2)})'

    def distance_to(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5

    @classmethod
    def origin(cls):
        return cls(0.0, 0.0)

    @classmethod
    def clone(cls, point):
        return cls(point.x, point.y)

    @classmethod
    def from_polar(cls, r, theta_degrees):
        x = r*cos(radians(theta_degrees))
        y = r*sin(radians(theta_degrees))
        return cls(x, y)

    @staticmethod
    def distance_between(p1, p2):
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5


p1 = Point2D(10, 12)
p2 = Point2D(0.5, 11.2)

#__str__ и __repr__
print(p1.__str__())
print(p2.__repr__())

#Методы
print('\nРасстояние между P1 и p2')
print(p1.distance_to(p2))

p1 = Point2D.origin()
p3 = Point2D.clone(p1)
print('\nСоздание клона p1 и сравнение адресов')
print(f'Адрес в памяти p1 - {id(p1)}')
print(f'Адрес в памяти p3 - {id(p3)}')

print('\nПеревод из полярных координат:')
print(Point2D.from_polar(10, 60))

print('\nИспользование статического метода')
p5 = (10, 15)
p6 = (0, 3)
print(Point2D.distance_between(p5, p6))

print('\nСчетчик объектов')
print(Point2D.total_points_count)