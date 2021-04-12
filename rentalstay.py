from datetime import date

class RentalStay:
    def __init__(self):
        self.source = ''
        self.id = 0
        self.renter = ''
        self.startDate = date.min
        self.endDate = date.min
        self.payout = 0.0
        self.bookingFee = 0.0

    def get_gross(self):
        return self.payout + self.bookingFee

    def get_identifier(self):
        return "{source}/{id:05d}".format(source=self.source, id=self.id)

    def parse_line(self, row):
        self.source = row["Source"]
        self.id = int(row["Id"])
        self.renter = row["Renter"]
        self.startDate = date.fromisoformat(row["Start Date"])
        self.endDate = date.fromisoformat(row["End Date"])
        self.payout = float(row["Payout"])
        self.bookingFee = float(row["Booking Fee"])
