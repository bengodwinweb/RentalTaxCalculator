from unittest import TestCase
import os

import taxcalculator.yearlytaxcalculator as tax_calc
from taxcalculator.yearlytax import YearlyTax

class Test(TestCase):
    def check_tax_assertions(self, yearly_tax: YearlyTax):
        self.assertAlmostEqual(2210.04, yearly_tax.gross, 2)
        self.assertAlmostEqual(1955.79, yearly_tax.taxableIncome, 2)
        self.assertAlmostEqual(1943.03, yearly_tax.quarter1.gross, 2)
        self.assertAlmostEqual(1719.50, yearly_tax.quarter1.taxableIncome, 2)
        self.assertAlmostEqual(5, yearly_tax.quarter1.nightsBooked)
        self.assertAlmostEqual(267.01, yearly_tax.quarter2.gross, 2)
        self.assertAlmostEqual(236.29, yearly_tax.quarter2.taxableIncome, 2)
        self.assertEqual(4, yearly_tax.quarter2.nightsBooked)
        self.assertEqual(0, yearly_tax.quarter3.gross)
        self.assertEqual(0, yearly_tax.quarter3.taxableIncome)
        self.assertEqual(0, yearly_tax.quarter3.nightsBooked)
        self.assertEqual(0, yearly_tax.quarter4.gross)
        self.assertEqual(0, yearly_tax.quarter4.taxableIncome)
        self.assertEqual(0, yearly_tax.quarter4.nightsBooked)


    def test_calc_year_url(self):
        config_file = 'files' + os.path.sep + 'config_test.json'
        url = 'https://docs.google.com/spreadsheets/d/1x07qhtWpfz0gDzYNhq--asq5zbrIkhIPAppy-51ri_4/edit#gid=0'
        yearly_tax = tax_calc.calc_year_url(config_file, url)
        self.check_tax_assertions(yearly_tax)


    def test_calc_year(self):
        config_file = 'files' + os.path.sep + 'config_test.json'
        csv_file = 'files' + os.path.sep + 'stays_test.csv'
        yearly_tax = tax_calc.calc_year_file(config_file, csv_file)
        self.check_tax_assertions(yearly_tax)


    def test_make_json(self):
        config_file = 'files' + os.path.sep + 'config_test.json'
        csv_file = 'files' + os.path.sep + 'stays_test.csv'
        yearly_tax = tax_calc.calc_year_file(config_file, csv_file)
        string = tax_calc.make_json(yearly_tax)
        print(string)  # no exceptions