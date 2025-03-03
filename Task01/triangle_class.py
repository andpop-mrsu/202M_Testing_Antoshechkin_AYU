class IncorrectTriangleSides(Exception):
    """Исключение, которое вызывается, если переданные стороны не образуют треугольник."""
    pass


class Triangle:
    def __init__(self, side1, side2, side3):
        """
        Конструктор класса Triangle.

        :param side1: Длина первой стороны треугольника
        :type side1: int или float
        :param side2: Длина второй стороны треугольника
        :type side2: int или float
        :param side3: Длина третьей стороны треугольника
        :type side3: int или float
        :raises IncorrectTriangleSides: Если переданные стороны не образуют треугольник
        """
        # Проверка, что все стороны положительны
        if any(side <= 0 for side in (side1, side2, side3)):
            raise IncorrectTriangleSides("Одна или несколько сторон имеют недопустимое значение.")

        # Проверка неравенства треугольника
        sides = sorted([side1, side2, side3])  # Сортируем стороны для удобства сравнения
        if sides[0] + sides[1] <= sides[2]:
            raise IncorrectTriangleSides("Переданные стороны не образуют треугольник.")

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def triangle_type(self):
        """
        Возвращает тип треугольника на основе длин его сторон.

        :return: Строка с типом треугольника
        :rtype: str
        """
        if self.side1 == self.side2 == self.side3:
            return "equilateral"  # Равносторонний треугольник
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "isosceles"  # Равнобедренный треугольник
        else:
            return "nonequilateral"  # Разносторонний треугольник

    def perimeter(self):
        """
        Возвращает периметр треугольника.

        :return: Периметр треугольника
        :rtype: float
        """
        return self.side1 + self.side2 + self.side3