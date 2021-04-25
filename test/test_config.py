from unittest import TestCase
import os

from taxcalculator.config import Config

class TestConfig(TestCase):
    def test_parse_file(self):
        fname = 'files' + os.path.sep + 'config_test.json'
        Config.parse_file(fname)
        self.assertEqual(2021, Config.YEAR)
        self.assertAlmostEqual(0.04, Config.OCCUPANCY_TAX)
        self.assertAlmostEqual(0.09, Config.SALES_TAX)
        self.assertEqual(True, Config.Q1.salesTaxPaidOnTime)
        self.assertEqual(True, Config.Q1.occupancyTaxPaidOnTime)
        self.assertEqual(False, Config.Q2.salesTaxPaidOnTime)
        self.assertEqual(True, Config.Q2.occupancyTaxPaidOnTime)
        self.assertEqual(True, Config.Q3.salesTaxPaidOnTime)
        self.assertEqual(False, Config.Q3.occupancyTaxPaidOnTime)
        self.assertEqual(False, Config.Q4.salesTaxPaidOnTime)
        self.assertEqual(False, Config.Q4.occupancyTaxPaidOnTime)
        self.assertEqual(0.03, Config.Q1.salesTaxOnTimeDiscount)
        self.assertEqual(0.03, Config.Q1.occupancyTaxOnTimeDiscount)
        self.assertEqual(0.05, Config.Q4.salesTaxOnTimeDiscount)
        self.assertEqual(0.06, Config.Q4.occupancyTaxOnTimeDiscount)

    def test_parse_file_not_found(self):
        fname = 'fooNotExist.json'
        Config.parse_file(fname)  # no exception
        self.assertEqual(2021, Config.YEAR)
        self.assertAlmostEqual(0.05, Config.OCCUPANCY_TAX)
        self.assertAlmostEqual(0.07, Config.SALES_TAX)
        self.assertEqual(True, Config.Q1.salesTaxPaidOnTime)
        self.assertEqual(True, Config.Q1.occupancyTaxPaidOnTime)
        self.assertEqual(True, Config.Q2.salesTaxPaidOnTime)
        self.assertEqual(True, Config.Q2.occupancyTaxPaidOnTime)
        self.assertEqual(True, Config.Q3.salesTaxPaidOnTime)
        self.assertEqual(True, Config.Q3.occupancyTaxPaidOnTime)
        self.assertEqual(True, Config.Q4.salesTaxPaidOnTime)
        self.assertEqual(True, Config.Q4.occupancyTaxPaidOnTime)
        self.assertEqual(0.03, Config.Q1.salesTaxOnTimeDiscount)
        self.assertEqual(0.03, Config.Q1.occupancyTaxOnTimeDiscount)
        self.assertEqual(0.03, Config.Q4.salesTaxOnTimeDiscount)
        self.assertEqual(0.03, Config.Q4.occupancyTaxOnTimeDiscount)
