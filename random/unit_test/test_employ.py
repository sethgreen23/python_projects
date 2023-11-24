import unittest
from employ import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print("setupClass")

	@classmethod
	def tearDownClass(cls):
		print("\ntearDowClass")

	def setUp(self):
		self.emp1 = Employee("Chaith", "Dridi", 5000)
		self.emp2 = Employee("Maria", "Dridi", 8000)

	def tearDown(self):
		pass
		
	def test_email(self):

		self.emp1.first = "Marious"
		self.emp2.first = "Carol"

		self.assertEqual(self.emp1.email, "Marious.Dridi@email.com")
		self.assertEqual(self.emp2.email, "Carol.Dridi@email.com")

	def test_full_name(self):
		
		self.assertEqual(self.emp1.fullname, "Chaith Dridi")
		self.assertEqual(self.emp2.fullname, "Maria Dridi")

		self.emp1.first = "Marious"
		self.emp2.first = "Carol"

		self.assertEqual(self.emp1.fullname, "Marious Dridi")
		self.assertEqual(self.emp2.fullname, "Carol Dridi")

	def test_pay(self):
		
		self.assertEqual(self.emp1.pay, 5000)
		self.assertEqual(self.emp2.pay, 8000)

		self.emp1.apply_raise()
		self.emp2.apply_raise()

		self.assertEqual(self.emp1.pay, 5250)
		self.assertEqual(self.emp2.pay, 8400)

	def test_monthly_schedule(self):
		#mock requests.get of employ module
		with patch('employ.requests.get') as mocked_get:
			#when we run the requests.get in employ module
			#it is using the mocked_get variable not the 
			#standard get
			#redirection of the request then we need to feed it
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'

			schedule = self.emp1.monthly_schedule("May")
			mocked_get.assert_called_with('http://company.com/Dridi/May')
			self.assertEqual(schedule, 'Success')

			mocked_get.return_value.ok = False
			schedule = self.emp2.monthly_schedule("June")
			mocked_get.assert_called_with("http://company.com/Dridi/June")
			self.assertEqual(schedule, 'Bad Response!')

if __name__ == '__main__':
	unittest.main()
