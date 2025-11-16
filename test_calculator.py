import unittest
from calculator import *



class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 4), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(-1, -4), 3)
    ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        self.assertAlmostEqual(divide(-9, 3), -3.0)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_logarithm(self):  # 3 assertions
        # log base 10 of 100 = 2
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        # log base 2 of 8 = 3
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        # log base 4 of 16 = 2
        self.assertAlmostEqual(logarithm(4, 16), 2.0)

    def test_log_invalid_base(self):  # 1 assertion
        # base 1 is invalid
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self):  # 3 assertions
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)
    




 

# Do not touch this
if __name__ == "__main__":
    unittest.main()