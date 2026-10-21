import unittest
import sys

from aoc2025.day5.day5 import foo, read_lines, process_ingredient_database, run, is_range_overlap, extend_range, run_2

class AocTests(unittest.TestCase):

    def test_stub_1(self):
        self.assertEqual(foo(), 1)

    def test_day5_read_lines_file_exists(self):
        """
        Test is passed when file exists
        """
        lines = read_lines('./tests/aoc2025/day5sample.txt')
        self.assertTrue(lines)

    def test_day5_read_lines_file_does_not_exist(self):
        """
        Test is passed if an error is raised when file does not exist
        """
        with self.assertRaises(FileNotFoundError) as e:
            lines = read_lines('filenotexists.txt')

    def test_day5_read_lines_must_be_str(self):
        """
        Test is passed if elements of the string are of str type
        """
        str_count = 0
        lines = read_lines('./tests/aoc2025/day5sample.txt')
        for l in lines:
            if type(l) is str:
                str_count += 1

        self.assertEqual(str_count, len(lines))

    def test_day5_process_ingredients_number(self):
        """
        Test is passed if the correct number of fresh_ids and avail_ids are created
        """
        database = read_lines('./tests/aoc2025/day5sample.txt')
        fresh_ids, avail_ids = process_ingredient_database(database)
        self.assertEqual(len(fresh_ids), 4)
        self.assertEqual(len(avail_ids), 6)

    def test_day5_process_ingredientstype(self):
        """
        Test is passed if the correct number of fresh_ids and avail_ids are created
        """
        database = read_lines('./tests/aoc2025/day5sample.txt')
        fresh_ids, avail_ids = process_ingredient_database(database)

        range_count = 0
        int_count = 0

        for i in fresh_ids:
            if isinstance(i, range):
                range_count += 1
            
        for i in avail_ids:
            if isinstance(i, int):
                int_count += 1

        self.assertEqual(len(fresh_ids), range_count)
        self.assertEqual(len(avail_ids), int_count)

    def test_day5_run(self):
        """
        Test is passed if result is 3
        """
        result = run('./tests/aoc2025/day5sample.txt')
        self.assertEqual(result, 3)

    def test_day5_is_rng_overlap_false(self):
        """
        Test is passed if is_range_overlap returns false
        """
        rng_a = range(10,15) # actual range is 10-14
        rng_b = range(16,21) # actual range is 16-20

        self.assertEqual(is_range_overlap(rng_a, rng_b), False)

    def test_day5_is_rng_overlap_true(self):
        """
        Test is passed if is_range_overlap returns true
        """
        rng_a = range(10,15) # actual range is 10-14
        rng_b = range(12,19) # actual range is 12-19

        self.assertEqual(is_range_overlap(rng_a, rng_b), True)

    def test_day5_is_rng_overlap_true_2(self):
        """
        Test is passed if is_range_overlap returns true
        Same end and start number
        """
        rng_a = range(10,15) # actual range is 10-14
        rng_b = range(14,19) # actual range is 14-19

        self.assertEqual(is_range_overlap(rng_a, rng_b), True)

    def test_day5_extend_range(self):
        """
        Test is passed if new range is extended
        """
        rng_a = range(10,15) # actual range is 10-14
        rng_b = range(12,19) # actual range is 12-19

        self.assertEqual(extend_range(rng_a, rng_b), range(10,19))

    def test_day5_extend_range_2(self):
        """
        Test is passed if new range is retained
        """
        rng_a = range(10,19) # actual range is 10-18
        rng_b = range(12,15) # actual range is 12-14

        self.assertEqual(extend_range(rng_a, rng_b), range(10,19))

    def test_day5_extend_range_error(self):
        """
        Test is passed if ValueError is raised
        """
        rng_a = range(1,5)   # actual range is 1-4
        rng_b = range(10,15) # actual range is 10-14


        with self.assertRaises(ValueError) as e:
            extend_range(rng_a, rng_b), range(10,19)

    def test_day5_run_2(self):
        """
        Test is passed if result is 14
        """
        result = run_2('./tests/aoc2025/day5sample.txt')
        self.assertEqual(result, 14)


if __name__ == '__main__':
    unittest.main()