import unittest
from io import StringIO
import sys
from decorator import CakeMaker, add_blueberries, add_chocolate_cream

class TestCakeMaker(unittest.TestCase):

    def setUp(self):
        self.baking = CakeMaker()
        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_make_base_cake_with_decorators(self):
        expected_output = "Making base cake\nAdding chocolate cream layer\nAdding blueberries on top\n"
        self.baking.make_base_cake()
        self.assertEqual(self.output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
