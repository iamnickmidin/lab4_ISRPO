import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    # Тестирует функцию area(r)
    # Аргументы:
    #   r (число): радиус круга
    # Проверяемая формула: S = π * r^2
    def test_area(self):
        res = area(5)
        self.assertAlmostEqual(res, math.pi * 25)

    # Тестирует функцию area(r) с дробным аргументом
    # Аргументы:
    #   r (число): радиус круга
    # Проверяемая формула: S = π * r^2
    def test_area_float(self):
        res = area(2.3)
        self.assertAlmostEqual(res, math.pi * (2.3 ** 2))

    # Тестирует функцию perimeter(r)
    # Аргументы:
    #   r (число): радиус круга
    # Проверяемая формула: P = 2πr
    def test_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 2 * math.pi * 5)

    # Тестирует функцию perimeter(r) с дробным аргументом
    # Аргументы:
    #   r (число): радиус круга
    # Проверяемая формула: P = 2πr
    def test_perimeter_float(self):
        res = perimeter(3.7)
        self.assertAlmostEqual(res, 2 * math.pi * 3.7)
