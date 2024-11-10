import convert
import unittest
import command_line

class TestCases(unittest.TestCase):
    #Tests for Task 1
    def test_str_to_float(self):
        input = "22.5"
        expected = 22.5
        result = convert.str_to_float(input)
        self.assertEqual(expected,result)
    def test_str_to_float_2(self):
        input = "Not a Float"
        expected = None
        result = convert.str_to_float(input)
        self.assertEqual(expected,result)


