import argparse
import sys
import os

import taxcalculator.csv as csv
import taxcalculator.pdf as pdf
import taxcalculator.net as net
from taxcalculator.config import Config
from taxcalculator.yearlytax import YearlyTax


def calc_year_file(config_location: str, csv_location: str) -> YearlyTax:
    print('Updating config from \"{}\"'.format(config_location))
    Config.parse_file(config_location)
    all_stays = csv.parse_stays(csv_location)
    yearly_tax = YearlyTax()
    yearly_tax.process_stays(all_stays)
    return yearly_tax


def calc_year_url(config_location: str, url: str) -> YearlyTax:
    temp_file = 'temp123456.csv'
    formatted_url = net.format_sheets_url(url)
    print('Fetching data from \"{}\"'.format(url))
    net.get_data(formatted_url, temp_file)
    yearly_tax = calc_year_file(config_location, temp_file)
    os.remove(temp_file)
    return yearly_tax


def make_json(yearly_tax: YearlyTax) -> str:
    return yearly_tax.toJSON()


def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-c', '--config')
    ap.add_argument('-u', '--url')
    ap.add_argument('-o', '--output')
    opt = ap.parse_args(args)
    yearly_tax = calc_year_url(opt.config, opt.url)
    pdf.make_pdf(opt.output, yearly_tax)
    print("Complete")
    # print(make_json(yearly_tax))


if __name__ == '__main__':
    main(sys.argv[1:])
