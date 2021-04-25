import json
import argparse
import sys

import taxcalculator.csv as csv
from taxcalculator.config import Config
from taxcalculator.yearlytax import YearlyTax


def calc_year(config_location, csv_location):
    Config.parse_file(config_location)
    all_stays = csv.parse_stays(csv_location)
    yearly_tax = YearlyTax()
    yearly_tax.process_stays(all_stays)
    return yearly_tax


def make_json(yearly_tax):
    return yearly_tax.toJSON()


def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-c', '--config')
    ap.add_argument('-f', '--file')
    opt = ap.parse_args(args)
    yearly_tax = calc_year(opt.config, opt.file)
    print(make_json(yearly_tax))


if __name__ == '__main__':
    main(sys.argv[1:])