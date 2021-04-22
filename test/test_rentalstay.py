import unittest
from datetime import date

from taxcalculator.rentalstay import RentalStay


class TestRentalStay(unittest.TestCase):
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


if __name__ == '__main__':
    TestRentalStay().test_GetQuarterJan()
