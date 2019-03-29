from unittest import TestCase
from listsuse import *


class TestList(TestCase):

    def test_largest_element(self):
        expected = 5123
        input_list = [1, 2, 3, 4, 5123, 6, 7]
        actual = largest_element(input_list)
        self.assertEqual(expected, actual)

    def test_largest_element_str(self):
        expected = "You're"
        input_list = ["Hi", "I", "Think", "That", "You're", "Cool"]
        actual = largest_element(input_list)
        self.assertEqual(expected, actual)

    def test_reverse_list(self):
        expected = [7, 6, 5, 4, 3, 2, 1]
        input_list = [1, 2, 3, 4, 5, 6, 7]
        actual = reverse_list(input_list)
        self.assertEqual(expected, actual)

    def test_reverse_list_str(self):
        expected = ["Hi", "I", "Think", "That", "You're", "Cool"]
        input_list = ["Cool", "You're", "That", "Think", "I", "Hi"]
        actual = reverse_list(input_list)
        self.assertEqual(expected, actual)

    def test_contains_true(self):
        element = 5
        input_list = [1, 2, 3, 4, 5, 6, 7]
        actual = contains(input_list, element)
        self.assertTrue(actual)

    def test_contains_false(self):
        element = 12
        input_list = [1, 2, 3, 4, 5, 6, 7]
        actual = contains(input_list, element)
        self.assertFalse(actual)

    def test_contains_true_str(self):
        element = "Cool"
        input_list = ["Hi", "I", "Think", "That", "You're", "Cool"]
        actual = contains(input_list, element)
        self.assertTrue(actual)

    def test_contains_false_str(self):
        element = "sorry, I'm not in there"
        input_list = ["Hi", "I", "Think", "That", "You're", "Cool"]
        actual = contains(input_list, element)
        self.assertFalse(actual)

    def test_odd_elements(self):
        input_list = ["Hi", "I", "Think", "That", "You're", "Cool"]
        expected = ["Hi", "Think", "You're"]
        actual = odd_elements(input_list)
        self.assertEqual(expected, actual)

    def test_odd_elements_int(self):
        input_list = [1, 2, 3, 4, 5, 6, 7]
        expected = [1, 3, 5, 7]
        actual = odd_elements(input_list)
        self.assertEqual(expected, actual)

    def test_total(self):
        input_list = [1, 2, 3, 4, 5, 6, 7]
        expected = 28
        actual = total(input_list)
        self.assertEqual(expected, actual)

    def test_total_floats(self):
        input_list = [1.5, 2.123, 3.23, 4, 5.645, 6.3, 7.9]
        expected = 30.698
        actual = total(input_list)
        self.assertEqual(expected, actual)

