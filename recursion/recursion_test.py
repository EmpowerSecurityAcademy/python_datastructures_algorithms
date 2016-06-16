import unittest
from recursion import factorial

class TestRecursion(unittest.TestCase):
	def test_factorial(self):
		four_factorial = factorial(4)

		self.assertEqual(four_factorial, 24)

if __name__ == '__main__':
	unittest.main(verbosity=2)