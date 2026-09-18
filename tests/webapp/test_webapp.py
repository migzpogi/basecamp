import unittest

from webapp import stub_1

class WebAppTests(unittest.TestCase):

    def test_stub_1(self):
        self.assertEqual(stub_1(), 1)

if __name__ == '__main__':
    unittest.main()