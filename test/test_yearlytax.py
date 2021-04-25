import os
from unittest import TestCase
from datetime import datetime

from taxcalculator.config import Config
from taxcalculator.rentalstay import RentalStay
from taxcalculator.yearlytax import YearlyTax
import taxcalculator.csv as csv

class TestYearlyTax(TestCase):
    def test_process_stays(self):
        # setup
        fname = 'files' + os.path.sep + 'stays_test.csv'
        stays = csv.parse_stays(fname)
        other_stay = RentalStay()
        other_stay.payout = 500
        other_stay.bookingFee = 50
        other_stay.transactionDate = datetime(2020, 12, 31)  # 2020, should be ignored
        stays.append(other_stay)
        Config.YEAR = 2021
        Config.OCCUPANCY_TAX = 0.05
        Config.SALES_TAX = 0.07
        tax_2021 = YearlyTax()

        # test
        tax_2021.process_stays(stays)
        self.assertAlmostEqual(2210.04, tax_2021.gross, 2)
        self.assertAlmostEqual(1973.25, tax_2021.taxableIncome, 2)
        self.assertAlmostEqual(1943.03, tax_2021.quarter1.gross, 2)
        self.assertAlmostEqual(1734.85, tax_2021.quarter1.taxableIncome, 2)
        self.assertAlmostEqual(5, tax_2021.quarter1.nightsBooked)
        self.assertAlmostEqual(267.01, tax_2021.quarter2.gross, 2)
        self.assertAlmostEqual(238.40, tax_2021.quarter2.taxableIncome, 2)
        self.assertAlmostEqual(4, tax_2021.quarter2.nightsBooked)
        self.assertEqual(0, tax_2021.quarter3.gross)
        self.assertEqual(0, tax_2021.quarter3.taxableIncome)
        self.assertEqual(0, tax_2021.quarter3.nightsBooked)
        self.assertEqual(0, tax_2021.quarter4.gross)
        self.assertEqual(0, tax_2021.quarter4.taxableIncome)
        self.assertEqual(0, tax_2021.quarter4.nightsBooked)


