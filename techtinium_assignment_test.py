import unittest
import techtinium_assignment

class TestAssignment(unittest.TestCase):

	def test_assignment(self):

		result = {'Output': [{'region': 'New York', 'total_cost': '$10150', 
		'machines': [('8XLarge', 7), ('Large', 1), ('XLarge', 1)]}, {'region': 'India', 
		'total_cost': '$9520', 'machines': [('8XLarge', 7), ('Large', 3)]}, 
		{'region': 'China', 'total_cost': '$8570', 'machines': [('8XLarge', 7), ('Large', 1), 
		('XLarge', 1)]}]}

		self.assertDictEqual(techtinium_assignment.assignment(1150, 1), result)

	def test_new_york_details(self):

		result = {'region': 'New York', 'total_cost': '$10150', 'machines': [('8XLarge', 7), 
		('Large', 1), ('XLarge', 1)]}
		self.assertDictEqual(techtinium_assignment.get_new_york_details(1150, 1), result)

	def test_india_details(self):

		result = {'region': 'India', 'total_cost': '$9520', 'machines': [('8XLarge', 7), 
		('Large', 3)]}
		self.assertDictEqual(techtinium_assignment.get_india_details(1150, 1), result)

	def test_china_details(self):

		result = {'region': 'China', 'total_cost': '$8570', 'machines': [('8XLarge', 7), 
		('Large', 1), ('XLarge', 1)]}
		self.assertDictEqual(techtinium_assignment.get_china_details(1150, 1), result)


if __name__ == "__main__":
	unittest.main()