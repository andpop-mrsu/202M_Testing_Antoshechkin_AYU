import math
import json


def solve_quadratic(a, b, c):
    # Проверка делителя на ноль
    if a == 0:
        return None  # Уравнение линейное, а не квадратное

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return sorted([root1, root2])
    elif discriminant == 0:
        root = -b / (2 * a)
        return [root]
    else:
        return []  # Нет вещественных корней


def load_tests1(filename):
    with open(filename, 'r') as file:
        tests = file.read().splitlines()
    return [json.loads(line) for line in tests if line.strip()]


def load_tests(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        tests = file.read().splitlines()
    parsed_tests = []
    for line in tests:
        if not line or line.startswith('#'):
            continue
        parts = line.replace('[', '').replace(']', '').replace(',', '').split()
        coefficients = list(map(float, parts[:3]))
        roots_str = parts[3:]
        if len(roots_str) == 1 and roots_str[0] == 'None':
            expected_roots = None
        elif len(roots_str) == 1 and roots_str[0] == '':
            expected_roots = []
        else:
            expected_roots = list(map(float, roots_str))
        parsed_tests.append((coefficients, expected_roots))
    return parsed_tests


def run_tests(tests):
    for test_case in tests:
        a, b, c = test_case[0][0], test_case[0][1], test_case[0][2]
        expected_result = test_case[1]

        result = solve_quadratic(a, b, c)
        assert result == expected_result, f"Тест {test_case} не пройден. Получено: {result}, ожидалось: {expected_result} "


if __name__ == "__main__":
    tests = load_tests('equation.txt')
    print("Запуск тестов...")
    run_tests(tests)
    print("Все тесты успешно завершены!")