
from taxcalculator.config import Config

class QuarterlyTax:

    def __init__(self, quarter_num):
        self.quarterNum = quarter_num
        self.nightsBooked = 0
        self.bookingFees = 0
        self.payout = 0
        self.gross = 0
        self.salesTaxCollected = 0
        self.salesTaxOwed = 0
        self.occupancyTaxCollected = 0
        self.occupancyTaxOwed = 0
        self.taxableIncome = 0

    def add_stays(self, stays):
        for stay in stays:
            if stay.get_quarter() == self.quarterNum:
                self.bookingFees += stay.bookingFee
                self.payout += stay.payout
                self.nightsBooked += stay.nights_booked()

        self.gross = self.bookingFees + self.payout
        self.taxableIncome = QuarterlyTax.calc_taxable_income(self.gross, Config.SALES_TAX, Config.OCCUPANCY_TAX)
        self.salesTaxCollected = self.taxableIncome * Config.SALES_TAX
        self.occupancyTaxCollected = self.taxableIncome * Config.OCCUPANCY_TAX
        self.salesTaxOwed = self.salesTaxCollected
        self.occupancyTaxOwed = self.occupancyTaxCollected

        q_config = Config.get_quarter(self.quarterNum)
        if q_config.salesTaxPaidOnTime:
            self.salesTaxOwed = self.salesTaxCollected - (self.salesTaxCollected * q_config.salesTaxOnTimeDiscount)
        if q_config.occupancyTaxPaidOnTime:
            self.occupancyTaxOwed = self.occupancyTaxCollected - (self.occupancyTaxCollected * q_config.occupancyTaxOnTimeDiscount)


    @staticmethod
    def calc_taxable_income(gross, sales_tax, occupancy_tax):
        return gross / (1 + sales_tax + occupancy_tax)
