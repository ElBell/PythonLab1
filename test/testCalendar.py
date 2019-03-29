from unittest import TestCase

from calprint import print_calendar


class TestCalendar(TestCase):
    def testPrintCal(self):
        expected = """    January 2025
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
"""
        actual = print_calendar(2025, 1)
        self.assertEqual(expected, actual)

    def test_print_today(self):
        expected = """     March 2019
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
"""
        actual = print_calendar(2019, 3)
        self.assertEqual(expected, actual)
