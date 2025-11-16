#https://github.com/dhruvpalli/lab10--DP---AJC-
#Partner 1 - Dhruv Palli
#Partner 2 - Ana Julia Cavaletti

import unittest
from calculator import *



class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 6), 8)
        self.assertEqual(add(-1, 7), 6)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(3, 6), -3)
        self.assertEqual(subtract(-1, -4), 3)
    ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(8, 2), 4)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        self.assertAlmostEqual(divide(-9, 3), -3.0)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(4, 16), 2.0)

    def test_log_invalid_base(self):  # 1 assertion
        # base 1 is invalid
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        
        with self.assertRaises(ValueError):
            logarithm(10, -4)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(6, 8), 10.0)
        self.assertAlmostEqual(hypotenuse(8, 15), 17.0)
        self.assertAlmostEqual(hypotenuse(0, 9), 9.0)

    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(1), 1.0)
        with self.assertRaises(ValueError):
            square_root(-5)
    




 

# Do not touch this
if __name__ == "__main__":
    unittest.main()
