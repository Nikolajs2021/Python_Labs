from gues_number_helper import isNotEqual, isInteger # import the functions for test

import unittest # call the function unittest

class TestInputValidation(unittest.TestCase): # creating for the test, testing the functions with different values
    def test_not_equlal_values(self):         # expected output TRUE when not equales pass
        self.assertTrue(isNotEqual(2, 3))     # the function acceptin 2 int and when it != returns TRUE
    def test_equal_valus(self):               # expected output FALSE when the values are equale
        self.assertFalse(isNotEqual(2, 2))    # the function acceptin 2 int and when it == returns FALSE
    def test_isInt(self):                     # checking the int and except one value
        self.assertTrue(isInteger(1))         # return TRUE when int pass
    def test_isNotInt(self):                  # checking the is not int and excepts one value
        self.assertFalse(isInteger('not int'))# return FALSE when  none int pass
