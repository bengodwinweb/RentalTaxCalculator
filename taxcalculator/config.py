import json


class QuarterConfig:
    def __init__(self,
                 sales_tax_on_time=True,
                 sales_tax_on_time_discount=0.03,
                 occupancy_tax_on_time=True,
                 occupancy_tax_on_time_discount=0.03):
        self.salesTaxPaidOnTime = sales_tax_on_time
        self.occupancyTaxPaidOnTime = occupancy_tax_on_time
        self.salesTaxOnTimeDiscount = sales_tax_on_time_discount
        self.occupancyTaxOnTimeDiscount = occupancy_tax_on_time_discount

    def update_from_dict(self, quarter_dict):
        self.salesTaxPaidOnTime = quarter_dict['SalesTaxPaidOnTime']
        self.salesTaxOnTimeDiscount = quarter_dict['SalesTaxOnTimeDiscount']
        self.occupancyTaxPaidOnTime = quarter_dict['OccupancyTaxPaidOnTime']
        self.occupancyTaxOnTimeDiscount = quarter_dict['OccupancyTaxOnTimeDiscount']


class Config:
    YEAR = 2021
    SALES_TAX = 0.07
    OCCUPANCY_TAX = 0.05
    Q1 = QuarterConfig()
    Q2 = QuarterConfig()
    Q3 = QuarterConfig()
    Q4 = QuarterConfig()

    @staticmethod
    def get_quarter(quarter_num):
        options = {
            1: Config.Q1,
            2: Config.Q2,
            3: Config.Q3,
            4: Config.Q4
        }
        return options[quarter_num]

    @staticmethod
    def parse_file(fname):
        try:
            with open(fname) as f:
                config_dict = json.load(f)
                Config.YEAR = config_dict['Year']
                Config.SALES_TAX = config_dict['SalesTax']
                Config.OCCUPANCY_TAX = config_dict['OccupancyTax']
                Config.Q1.update_from_dict(config_dict['Quarter1'])
                Config.Q2.update_from_dict(config_dict['Quarter2'])
                Config.Q3.update_from_dict(config_dict['Quarter3'])
                Config.Q4.update_from_dict(config_dict['Quarter4'])
        except FileNotFoundError:
            # reset to defaults if file not found
            print("File \"" + fname + "\" not found")
            Config.YEAR = 2021
            Config.SALES_TAX = 0.07
            Config.OCCUPANCY_TAX = 0.05
            Config.Q1 = QuarterConfig()
            Config.Q2 = QuarterConfig()
            Config.Q3 = QuarterConfig()
            Config.Q4 = QuarterConfig()
