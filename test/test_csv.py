import unittest
import os

import taxcalculator.csv as csv

class TestCsv(unittest.TestCase):
    def test_splitLine(self):
        line = '  1,2,3,,a,4,asdfasdfasdf\t'
        split = csv.split_line(line)
        self.assertEqual(7, len(split))
        self.assertEqual('1', split[0])
        self.assertEqual('2', split[1])
        self.assertEqual('3', split[2])
        self.assertEqual('', split[3])
        self.assertEqual('a', split[4])
        self.assertEqual('4', split[5])
        self.assertEqual('asdfasdfasdf', split[6])

    def test_parseStays(self):
        fname = 'files' + os.path.sep + 'stays_test.csv'
        stays = csv.parse_stays(fname)
        self.assertEqual(3, len(stays))
        self.assertEqual(67.32, stays[0].bookingFee)

    def test_sortBy(self):
        row1 = { 'Field1': '2', 'Field2': 'a' }
        row2 = { 'Field1': '1', 'Field2': 'c' }
        row3 = { 'Field1': '3', 'Field2': 'b' }
        list = [row1, row2, row3]
        list = csv.sort_by(list, 'Field1', True)
        self.assertEqual('3', list[0]['Field1'])
        self.assertEqual('2', list[1]['Field1'])
        self.assertEqual('1', list[2]['Field1'])
        list = csv.sort_by(list, 'Field2', False)
        self.assertEqual('a', list[0]['Field2'])
        self.assertEqual('b', list[1]['Field2'])
        self.assertEqual('c', list[2]['Field2'])