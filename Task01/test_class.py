import pytest
from triangle_class import Triangle, IncorrectTriangleSides

# Позитивные тесты
@pytest.mark.parametrize(
    "side1, side2, side3, expected_type",
    [
        (3, 4, 5, "nonequilateral"),      # Разносторонний треугольник
        (3, 3, 3, "equilateral"),          # Равносторонний треугольник
        (3, 3, 4, "isosceles"),            # Равнобедренный треугольник
        (5, 12, 13, "nonequilateral"),     # Прямоугольный треугольник
    ]
)
def test_triangle_type_positive(side1, side2, side3, expected_type):
    triangle = Triangle(side1, side2, side3)
    assert triangle.triangle_type() == expected_type


# Негативные тесты (создание треугольников с неверными данными)
@pytest.mark.parametrize(
    "side1, side2, side3, exception_message",
    [
        (0, 1, 1, "Одна или несколько сторон имеют недопустимое значение."),   # Сторона равна нулю
        (-1, 1, 1, "Одна или несколько сторон имеют недопустимое значение."),  # Отрицательная сторона
        (1, 1, 3, "Переданные стороны не образуют треугольник."),              # Нарушено неравенство треугольника
    ]
)
def test_triangle_creation_negative(side1, side2, side3, exception_message):
    with pytest.raises(IncorrectTriangleSides) as excinfo:
        Triangle(side1, side2, side3)
    assert exception_message in str(excinfo.value)


# Тестирование метода периметра
@pytest.mark.parametrize(
    "side1, side2, side3, expected_perimeter",
    [
        (3, 4, 5, 12),
        (3, 3, 3, 9),
        (5, 12, 13, 30),
    ]
)
def test_perimeter(side1, side2, side3, expected_perimeter):
    triangle = Triangle(side1, side2, side3)
    assert triangle.perimeter() == expected_perimeter