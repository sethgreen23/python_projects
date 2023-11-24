import unittest
import calc

class TestClac(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc.add(10, 15), 25)
		self.assertEqual(calc.add(-1, 1), 0)
		self.assertEqual(calc.add(-1, -1), -2)
	def test_sub(self):
		self.assertEqual(calc.sub(10, 15), -5)
		self.assertEqual(calc.sub(-1, 1), -2)
		self.assertEqual(calc.sub(-1, -1), 0)
	def test_mul(self):
		self.assertEqual(calc.mul(10, 15), 150)
		self.assertEqual(calc.mul(-1, 1), -1)
		self.assertEqual(calc.mul(-1, -1), 1)
	def test_div(self):
		self.assertEqual(calc.div(10, 5), 2)
		self.assertEqual(calc.div(-1, 1), -1)
		self.assertEqual(calc.div(-1, -1), 1)

		#assert the raise error
		#self.assertRaises(ZeroDivisionError, calc.div, 10, 0)
		#better way is to use context manager
		with self.assertRaises(ZeroDivisionError):
			calc.div(10, 0)
if __name__ == "__main__":
	unittest.main()
