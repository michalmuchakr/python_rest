"""
Sample test
"""
from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test case - example"""

    def test_add_numbers(self):
        """Test adding two number"""
        res = calc.add(1, 3)

        self.assertEqual(res, 4)

    def test_subtrack_numbers(self):
        """Test """
        res = calc.subtrack(10, 15)
        self.assertEqual(res, 5)
