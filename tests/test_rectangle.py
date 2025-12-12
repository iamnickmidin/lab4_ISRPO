import unittest
from rectange import area, perimeter   # если файл rectangle.py — исправь импорт


class RectangleTestCase(unittest.TestCase):

    # Тестирует функцию area(a, b)
    # Аргументы:
    #   a (число): длина первой стороны прямоугольника
    #   b (число): длина второй стороны прямоугольника
    # Проверяемая формула: S = a * b
    def test_area(self):
        res = area(5, 3)
        self.assertEqual(res, 15)

    # Тестирует функцию area(a, b) с дробными значениями
    # Аргументы:
    #   a (число): длина первой стороны прямоугольника
    #   b (число): длина второй стороны прямоугольника
    # Проверяемая формула: S = a * b
    def test_area_float(self):
        res = area(2.5, 4.2)
        self.assertAlmostEqual(res, 2.5 * 4.2)

    # Тестирует функцию perimeter(a, b)
    # Аргументы:
    #   a (число): длина первой стороны прямоугольника
    #   b (число): длина второй стороны прямоугольника
    # Проверяемая формула: P = 2(a + b)
    def test_perimeter(self):
        res = perimeter(5, 3)
        self.assertEqual(res, 16)

    # Тестирует функцию perimeter(a, b) с дробными значениями
    # Аргументы:
    #   a (число): длина первой стороны
    #   b (число): длина второй стороны
    # Проверяемая формула: P = 2(a + b)
    def test_perimeter_float(self):
        res = perimeter(2.5, 4.2)
        self.assertAlmostEqual(res, 2 * (2.5 + 4.2))
