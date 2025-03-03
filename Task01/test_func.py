import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


def read_test_data(file_path):
    test_cases = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue  # Пропускаем пустые строки и комментарии

            data = line.split('- ')  # Разбиваем строку на две части
            coefficients = tuple(map(float, data[0].strip('[]').split(',')))  # Парсим стороны треугольника
            expected_result = data[1].strip('"')  # Парсим ожидаемый результат
            test_cases.append((coefficients, expected_result))

    return test_cases


class TestTriangleType(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_data = read_test_data('check.txt')

    def test_get_triangle_type(self):
        for case in self.test_data:
            sides, expected = case
            try:
                result = get_triangle_type(*sides)
                self.assertEqual(result, expected)
            except IncorrectTriangleSides as e:
                self.assertIn(expected, str(e))


if __name__ == '__main__':
    unittest.main()