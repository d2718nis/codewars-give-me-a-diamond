from unittest import TestCase
from src.main import diamond


class DiamondTestCase(TestCase):
    """Diamond related tests."""

    def test_diamond_with_n_3(self):
        """diamond() returns diamond-shaped string of size 3."""
        expected =  " *\n***\n *\n"
        self.assertEqual(diamond(3), expected)

    def test_diamond_with_n_negative(self):
        """diamond() returns None for the negative n."""
        self.assertEqual(diamond(-1), None)

    def test_diamond_with_n_even(self):
        """diamond() returns None for the even n."""
        self.assertEqual(diamond(4), None)
