class IncorrectTriangleSides(Exception):
    """Исключение, которое вызывается, если переданные стороны не образуют треугольник."""
    pass


def get_triangle_type(side1, side2, side3):
    """
    Возвращает тип треугольника на основе длин его сторон.

    :param side1: Длина первой стороны треугольника
    :type side1: int или float
    :param side2: Длина второй стороны треугольника
    :type side2: int или float
    :param side3: Длина третьей стороны треугольника
    :type side3: int или float
    :return: Строка с типом треугольника
    :rtype: str
    :raises IncorrectTriangleSides: Если переданные стороны не образуют треугольник

    >>> get_triangle_type(3, 4, 5)
    'nonequilateral'
    >>> get_triangle_type(3, 3, 3)
    'equilateral'
    >>> get_triangle_type(3, 3, 4)
    'isosceles'
    >>> try:
    ...     get_triangle_type(0, 1, 1)
    ... except IncorrectTriangleSides as e:
    ...     print(str(e))
    'Одна или несколько сторон имеют недопустимое значение.'
    >>> try:
    ...     get_triangle_type(1, 1, 3)
    ... except IncorrectTriangleSides as e:
    ...     print(str(e))
    'Переданные стороны не образуют треугольник.'
    """

    # Проверка, что все стороны положительны
    if any(side < 1 for side in (side1, side2, side3)):
        raise IncorrectTriangleSides("Одна или несколько сторон имеют недопустимое значение.")

    # Проверка неравенства треугольника
    sides = sorted([side1, side2, side3])  # Сортируем стороны для удобства сравнения
    if sides[0] + sides[1] <= sides[2]:
        raise IncorrectTriangleSides("Переданные стороны не образуют треугольник.")

    # Определение типа треугольника
    if side1 == side2 == side3:
        return "equilateral"  # Равносторонний треугольник
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"  # Равнобедренный треугольник
    else:
        return "nonequilateral"  # Разносторонний треугольник