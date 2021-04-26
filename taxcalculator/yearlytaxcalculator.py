import argparse
import sys

import taxcalculator.csv as csv
import taxcalculator.pdf as pdf
from taxcalculator.config import Config
from taxcalculator.yearlytax import YearlyTax


def calc_year(config_location: str, csv_location: str) -> YearlyTax:
    Config.parse_file(config_location)
    all_stays = csv.parse_stays(csv_location)
    yearly_tax = YearlyTax()
    yearly_tax.process_stays(all_stays)
    return yearly_tax


def make_json(yearly_tax: YearlyTax) -> str:
    return yearly_tax.toJSON()


def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-c', '--config')
    ap.add_argument('-f', '--file')
    ap.add_argument('-o', '--output')
    opt = ap.parse_args(args)
    yearly_tax = calc_year(opt.config, opt.file)
    pdf.make_pdf(opt.output, yearly_tax)
    # print(make_json(yearly_tax))


if __name__ == '__main__':
    main(sys.argv[1:])