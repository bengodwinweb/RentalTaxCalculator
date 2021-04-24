

class QuarterlyTax:
    SALES_TAX = 0.07
    OCCUPANCY_TAX = 0.05
    SALES_TAX_ON_TIME_DISCOUNT = 0.03
    OCCUPANCY_TAX_ON_TIME_DISCOUNT = 0.03

    def __init__(self, quarter_num, sales_tax_on_time=True, occupancy_tax_on_time=True):
        self.quarterNum = quarter_num
        self.salesTaxPaidOnTime = sales_tax_on_time
        self.occupancyTaxPaidOnTime = occupancy_tax_on_time
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
        self.taxableIncome = QuarterlyTax.calc_taxable_income(self.gross, QuarterlyTax.SALES_TAX, QuarterlyTax.OCCUPANCY_TAX)
        self.salesTaxCollected = self.taxableIncome * QuarterlyTax.SALES_TAX
        self.occupancyTaxCollected = self.taxableIncome * QuarterlyTax.OCCUPANCY_TAX
        self.salesTaxOwed = self.salesTaxCollected
        self.occupancyTaxOwed = self.occupancyTaxCollected

        if self.salesTaxPaidOnTime:
            self.salesTaxOwed = self.salesTaxCollected - (self.salesTaxCollected * QuarterlyTax.SALES_TAX_ON_TIME_DISCOUNT)
        if self.occupancyTaxPaidOnTime:
            self.occupancyTaxOwed = self.occupancyTaxCollected - (self.occupancyTaxCollected * QuarterlyTax.OCCUPANCY_TAX_ON_TIME_DISCOUNT)


    @staticmethod
    def calc_taxable_income(gross, sales_tax, occupancy_tax):
        return gross / (1 + sales_tax + occupancy_tax)
