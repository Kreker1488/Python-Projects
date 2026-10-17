from math import radians, cos, sin

class Point3D:
    total_points_count = 0
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        Point3D.total_points_count += 1

    def __str__(self):
        return f'({round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)})'

    def __repr__(self):
        return f'Point3D(x={round(self.x, 2)}, y={round(self.y, 2)}, z={round(self.z, 2)})'

    def distance_to(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2)**0.5

    @classmethod
    def origin(cls):
        return cls(0.0, 0.0, 0.0)

    @classmethod
    def clone(cls, point):
        return cls(point.x, point.y, point.z)

    @classmethod
    def from_polar(cls, r, theta_degrees, phi_degrees):
        x = r*cos(radians(theta_degrees))*cos(radians(phi_degrees))
        y = r*sin(radians(theta_degrees))*cos(radians(phi_degrees))
        z = r*sin(radians(phi_degrees))
        return cls(x, y, z)

    @staticmethod
    def distance_between(p1, p2):
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)**0.5

class Vector3D:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return f'({round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)})'

    def __repr__(self):
        return f'Vector3D(x={round(self.x, 2)}, y={round(self.y, 2)}, z={round(self.z, 2)})'

    def _vector_len(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    @classmethod
    def from_points(cls, start, end):
        return cls(end.x - start.x, end.y - start.y, end.z - start.z)

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __gt__(self, other):
        return self._vector_len() > other._vector_len()

    def __lt__(self, other):
        return self._vector_len() < other._vector_len()

    #СЛОЖЕНИЕ
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x + other, self.y + other, self.z + other)
        else:
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __radd__(self, other):
        return self.__add__(other)

    #УМНОЖЕНИЕ
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        else:
            return Vector3D(self.x * other.x, self.y * other.y, self.z * other.z)
    def __rmul__(self, other):
        return self.__mul__(other)

    #ВЫЧИТАНИЕ
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x - other, self.y - other, self.z - other)
        else:
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __rsub__(self, other):
        return self.__sub__(other)*(-1)

    #ДЕЛЕНИЕ
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x / other, self.y / other, self.z / other)
        else:
            return Vector3D(self.x / other.x, self.y / other.y, self.z / other.z)
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(other / self.x, other / self.y, other / self.z)
        else:
            return Vector3D(self.x / other.x, self.y / other.y, self.z / other.z)

    #СЛОЖЕНИЕ НА МЕСТЕ
    def __iadd__(self, other):
        if isinstance(other, (int, float)):
            self.x += other
            self.y += other
            self.z += other
        else:
            self.x += other.x
            self.y += other.y
            self.z += other.z
        return self

    #ВЫЧИТАНИЕ НА МЕСТЕ
    def __isub__(self, other):
        if isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
            self.z -= other
        else:
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        return self

    #УМНОЖЕНИЕ НА МЕСТЕ
    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            self.z *= other
        else:
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        return self

    #ДЕЛЕНИЕ НА МЕСТЕ
    def __itruediv__(self, other):
        if isinstance(other, (int, float)):
            self.x /= other
            self.y /= other
            self.z /= other
        else:
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        return self

    def __matmul__(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def __getitem__(self, item):
        cords = (self.x, self.y, self.z)

        if isinstance(item, int):
            return cords[item]
        elif isinstance(item, str):
            mapping = {'x': 0, 'y': 1, 'z': 2}
            return cords[mapping[item]]

    #ИТЕРАТОР
    def __iter__(self):
        return iter((self.x, self.y, self.z))


# 1. Точки и счетчик
p1 = Point3D(1, 2, 3)
p2 = Point3D.origin()
p3 = Point3D.clone(p1)
print(f"Точки: {p1}, {p2}, {p3} | Всего: {Point3D.total_points_count}")

# 2. Векторы, длина и создание по точкам
v1 = Vector3D(1, 2, 3)
v2 = Vector3D.from_points(p1, p2)
print(f"\nВекторы: {v1}, {v2} | Длина: {v1._vector_len():}")

# 3. Арифметика (векторы и числа)
print(f"\nАрифметика: {v1 + v2}, {v1 - 5}, {5 - v1}, {2 * v1}, {v1 / 2}, {2 / v1}")

# 4. Сравнения
print(f"Сравнения: v1 == v2 -> {v1 == v2}, v1 < v2 -> {v1 < v2}")

# 5. Операции на месте (проверка id)
v3 = Vector3D(1, 1, 1)
old_id = id(v3)
v3 += 10
v3 *= 2
print(f"\nIn-place: {v3} | Объект тот же? {id(v3) == old_id}")

# 6. Спец. операции и доступ
cross = Vector3D(1, 0, 0) @ Vector3D(0, 1, 0)
print(f"\nВекторное: {cross}")
print(f"Индексы: {v1[0]}, {v1['z']} | Перебор: {list(v1)}")