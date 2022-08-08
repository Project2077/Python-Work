# Write a test case for Employee. Write two test methods, test_give_default
# _raise() and test_give_custom_raise(). Use the setUp() method so you don’t
# have to create a new employee instance in each test method. Run your test
# case, and make sure both tests pass.
from Employee import Employee as emp
import unittest


class TestEmployeeCase(unittest.TestCase):
    def setUp(self):
        self.employee = emp("Eric", "Matthes", 0)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 5000)

    def test_give_custom_raise(self):
        self.employee.give_raise(8000)
        self.assertEqual(self.employee.annual_salary, 8000)


if __name__ == '__main__':
    unittest.main()