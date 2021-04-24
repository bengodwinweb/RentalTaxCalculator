from taxcalculator.rentalstay import RentalStay

def split_line(line):
    """
    Splits a line of CSV text into an array of values
    """
    return line.strip().split(',')

def parse_stays(fname):
    """
    Parses a csv file into a list of dictionaries. All values remain strings
    """
    with open(fname, encoding='utf8') as fin:
        stays = []
        for i, line in enumerate(fin):
            values = split_line(line)
            if i == 0:
                headers = values;
            else:
                row = dict(zip(headers, values))
                stay = RentalStay()
                stay.parse_line(row)
                stays.append(stay)
    return stays;

def sort_by(rows, col_name, rev):
    """
    Sorts rows of dictionaries by the value in a particular key (col_name).
    rev is a boolean indicating whether the order should be reversed.
    """
    def get_col(row):
        return row[col_name]
    return sorted(rows, key=get_col, reverse=rev)
