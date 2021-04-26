from unittest import TestCase
import os

import taxcalculator.net as net
import taxcalculator.csv as csv


class Test(TestCase):
    def setUp(self) -> None:
        self.fname = 'files' + os.path.sep + 'tempdata.csv'


    def tearDown(self) -> None:
        if os.path.exists(self.fname):
            os.remove(self.fname)


    def test_format_sheets_url(self):
        test_url = 'https://docs.google.com/spreadsheets/d/1x07qhtWpfz0gDzYNhq--asq5zbrIkhIPAppy-51ri_4/edit#gid=0'
        formatted = net.format_sheets_url(test_url)
        self.assertEqual('https://docs.google.com/spreadsheets/d/1x07qhtWpfz0gDzYNhq--asq5zbrIkhIPAppy-51ri_4/pub?output=csv', formatted)


    def test_get_data(self):
        url = "https://docs.google.com/spreadsheets/d/1x07qhtWpfz0gDzYNhq--asq5zbrIkhIPAppy-51ri_4/pub?output=csv"
        net.get_data(url, self.fname)
        stays = csv.parse_stays(self.fname)
        self.assertEqual(3, len(stays))
