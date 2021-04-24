import unittest
from datetime import date

from taxcalculator.rentalstay import RentalStay


class TestRentalStay(unittest.TestCase):
    def test_getIdentifier(self):
        stay = RentalStay()
        stay.source = 'AirBnb'
        stay.id = 1
        self.assertEqual('AirBnb/00001', stay.get_identifier())

    def test_getGross(self):
        stay = RentalStay()
        stay.bookingFee = 111.11
        stay.payout = 222.22
        self.assertEqual(333.33, stay.get_gross())

    def test_parseLine(self):
        row = {
            'Source': 'Vrbo',
            'Id': '12345',
            'Renter': 'Johnson',
            'Transaction Date': '2021-04-22',
            'Start Date': '2021-03-31',
            'End Date': '2021-04-02',
            'Payout': '123.45',
            'Booking Fee': '11.69',
        }
        stay = RentalStay()
        stay.parse_line(row)
        self.assertEqual('Vrbo', stay.source, 'Source')
        self.assertEqual(12345, stay.id, 'Id')
        self.assertEqual('Vrbo/12345', stay.get_identifier(), 'Identifier')
        self.assertEqual('Johnson', stay.renter, 'Renter')
        self.assertEqual(date(2021, 4, 22), stay.transactionDate, 'Transaction Date')
        self.assertEqual(2, stay.get_quarter(), 'Quarter')
        self.assertEqual(date(2021, 3, 31), stay.startDate, 'Start Date')
        self.assertEqual(date(2021, 4, 2), stay.endDate, 'End Date')
        self.assertAlmostEqual(123.45, stay.payout, 7, 'Payout')
        self.assertAlmostEqual(11.69, stay.bookingFee, 7, 'Booking Fee')
        self.assertAlmostEqual(135.14, stay.get_gross(), 7, 'Gross')

    def test_GetQuarterJan(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 1, 1)
        self.assertEqual(1, stay.get_quarter())

    def test_GetQuarterFeb(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 2, 1)
        self.assertEqual(1, stay.get_quarter())

    def test_GetQuarterMar(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 3, 1)
        self.assertEqual(1, stay.get_quarter())
        stay.transactionDate = date(2021, 3, 31)
        self.assertEqual(1, stay.get_quarter())

    def test_GetQuarterApr(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 4, 1)
        self.assertEqual(2, stay.get_quarter())

    def test_GetQuarterMay(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 5, 1)
        self.assertEqual(2, stay.get_quarter())

    def test_GetQuarterJun(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 6, 1)
        self.assertEqual(2, stay.get_quarter())

    def test_GetQuarterJul(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 7, 1)
        self.assertEqual(3, stay.get_quarter())

    def test_GetQuarterAug(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 8, 1)
        self.assertEqual(3, stay.get_quarter())

    def test_GetQuarterSep(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 9, 1)
        self.assertEqual(3, stay.get_quarter())

    def test_GetQuarterOct(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 10, 1)
        self.assertEqual(4, stay.get_quarter())

    def test_GetQuarterNov(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 11, 1)
        self.assertEqual(4, stay.get_quarter())

    def test_GetQuarterDec(self):
        stay = RentalStay()
        stay.transactionDate = date(2021, 12, 1)
        self.assertEqual(4, stay.get_quarter())