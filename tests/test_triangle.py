import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    # Тестирует функцию area(a, h)
    # Аргументы:
    #   a (число): основание треугольника
    #   h (число): высота, опущенная на основание a
    # Проверяемая формула: S = (a * h) / 2
    def test_area(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    # Тестирует функцию area(a, h) с дробными аргументами
    # Аргументы:
    #   a (число): основание
    #   h (число): высота
    # Проверяемая формула: S = (a * h) / 2
    def test_area_float(self):
        res = area(3.2, 7.1)
        self.assertAlmostEqual(res, (3.2 * 7.1) / 2)

    # Тестирует функцию perimeter(a, b, c)
    # Аргументы:
    #   a (число): первая сторона треугольника
    #   b (число): вторая сторона треугольника
    #   c (число): третья сторона треугольника
    # Проверяемая формула: P = a + b + c
    def test_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    # Тестирует функцию perimeter(a, b, c) с дробными значениями
    # Аргументы:
    #   a (число): первая сторона
    #   b (число): вторая сторона
    #   c (число): третья сторона
    # Проверяемая формула: P = a + b + c
    def test_perimeter_float(self):
        res = perimeter(2.5, 3.7, 4.1)
        self.assertAlmostEqual(res, 2.5 + 3.7 + 4.1)
