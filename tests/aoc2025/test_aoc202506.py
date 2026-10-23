import unittest
import sys

from aoc2025.day6.day6 import foo, prepare_problem_input

class AocTests(unittest.TestCase):
    def test_stub_1(self):
        self.assertEqual(foo(), 1)

    def test_prepare_problem_input(self):
        """
        Test is passed if number of elements are equal 
        """
        line = '123 328  51 64'

        self.assertEqual(len(prepare_problem_input(line)), 4)

    def test_prepare_problem_input_integer(self):
        """
        Test is passed if elements are of integer type
        """
        line = '123 328  51 64'

        self.assertEqual(prepare_problem_input(line)[1], 328)

    def test_prepare_problem_input_string(self):
        """
        Test is passed if elements are of str type
        """
        line = '*   +   *   + '

        self.assertEqual(prepare_problem_input(line)[1], '+')

if __name__ == '__main__':
    unittest.main()