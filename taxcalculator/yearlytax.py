import json

from taxcalculator.config import Config
from taxcalculator.quarterlytax import QuarterlyTax

class YearlyTax:
    def __init__(self):
        self.quarter1 = QuarterlyTax(1)
        self.quarter2 = QuarterlyTax(2)
        self.quarter3 = QuarterlyTax(3)
        self.quarter4 = QuarterlyTax(4)
        self.year = Config.YEAR
        self.gross = 0
        self.taxableIncome = 0
        self.nightsBooked = 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def process_stays(self, stays):
        year_stays = [stay for stay in stays if stay.transactionDate.year == Config.YEAR]
        quarters = [self.quarter1, self.quarter2, self.quarter3, self.quarter4]
        for q in quarters:
            q.add_stays(year_stays)
            self.gross += q.gross
            self.taxableIncome += q.taxableIncome
            self.nightsBooked += q.nightsBooked
