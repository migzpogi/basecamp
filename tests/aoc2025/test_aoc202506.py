import unittest
import sys

from aoc2025.day6.day6 import foo, prepare_problem_input, HomeWork, run_1

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

    def test_homework(self):
        """
        Test is passed if assertions regarding Homework are equal
        """
        e1 = [123, 328, 51, 64]
        e2 = [45, 64, 387, 23]
        e3 = [6, 98, 215, 314]
        e4 = ['*', '+', '*', '+']

        h = HomeWork()

        h.add_elements(e1)
        h.add_elements(e2)
        h.add_elements(e3)
        h.add_operators(e4)

        self.assertEqual(len(h.matrix), 3)
        self.assertEqual(len(h.operators), 4)
        self.assertEqual(h.get_element(0,0), 123)
        self.assertEqual(h.get_element(2,3), 314)
        self.assertEqual(h.x_size, 3)
        self.assertEqual(h.y_size, 4)
        self.assertEqual(h.compute_column(0), 33210)
        self.assertEqual(h.compute_column(1), 490)
        self.assertEqual(h.compute_homework(), 4277556)

    def test_run_1(self):
        """
        Test is passed if answer = 4277556
        """
        result = run_1('./tests/aoc2025/day6sample.txt')
        self.assertEqual(result, 4277556)


if __name__ == '__main__':
    unittest.main()