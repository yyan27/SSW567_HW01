"""automated tests for Yan_HW01"""

import unittest
from Yan_HW01 import classify_triangle

class HW01Test(unittest.TestCase):

    def test_classify_triangle_scalene_right(self) -> None:
        self.assertEqual(classify_triangle(3, 4, 5), "It is a scalene triangle, and a right triangle.")

    def test_classify_triangle_scalene(self) -> None:
        self.assertEqual(classify_triangle(3, 4, 6), "It is a scalene triangle, but not a right triangle.")

    def test_classify_triangle_isosceles(self) -> None:
        self.assertEqual(classify_triangle(4, 4, 6), "It is an isosceles triangle, but not a right triangle.")

    def test_classify_triangle_equilateral(self) -> None:
        self.assertEqual(classify_triangle(4, 4, 4), "It is an equilateral triangle, but not a right triangle.")

if __name__ == "__main__":
    """main function"""
    unittest.main(exit=False, verbosity=2)