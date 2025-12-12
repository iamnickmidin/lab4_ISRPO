import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    # Тестирует функцию area(a)
    # Аргументы:
    #   a (число): длина стороны квадрата
    # Проверяемая формула: S = a^2
    def test_area(self):
        res = area(4)
        self.assertEqual(res, 16)

    # Тестирует функцию area(a) с дробным аргументом
    # Аргументы:
    #   a (число): длина стороны квадрата
    # Проверяемая формула: S = a^2
    def test_area_float(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 2.5 * 2.5)

    # Тестирует функцию perimeter(a)
    # Аргументы:
    #   a (число): длина стороны квадрата
    # Проверяемая формула: P = 4a
    def test_perimeter(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    # Тестирует функцию perimeter(a) с дробным аргументом
    # Аргументы:
    #   a (число): длина стороны квадрата
    # Проверяемая формула: P = 4a
    def test_perimeter_float(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 4 * 2.5)
