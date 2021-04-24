from unittest import TestCase
import os

from taxcalculator.quarterlytax import QuarterlyTax
import taxcalculator.csv as csv


class TestQuarterlyTax(TestCase):
    def test_calTaxableIncome(self):
        self.assertAlmostEqual(89.29, QuarterlyTax.calc_taxable_income(100, 0.07, 0.05), 2)

    def test_addStays(self):
        quarter = QuarterlyTax(1)
        fname = 'files' + os.path.sep + 'stays_test.csv'
        ytd_stays = csv.parse_stays(fname)
        quarter.add_stays(ytd_stays)
        self.assertAlmostEqual(89.62, quarter.bookingFees, 2)
        self.assertAlmostEqual(1853.41, quarter.payout, 2)
        self.assertAlmostEqual(1943.03, quarter.gross, 2)
        self.assertEqual(5, quarter.nightsBooked)
        self.assertAlmostEqual(1734.85, quarter.taxableIncome, 2)
        self.assertAlmostEqual(121.44, quarter.salesTaxCollected, 2)
        self.assertAlmostEqual(86.74, quarter.occupancyTaxCollected, 2)
        self.assertAlmostEqual(117.80, quarter.salesTaxOwed, 2)
        self.assertAlmostEqual(84.14, quarter.occupancyTaxOwed, 2)
