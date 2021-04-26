from taxcalculator.rentalstay import RentalStay


def split_line(line: str) -> [str]:
    """
    Splits a line of CSV text into an array of values
    @param line: values separated by commas
    @type line: str
    @return: list of values
    @rtype: [str]
    """
    return line.strip().split(',')


def parse_stays(fname: str) -> [RentalStay]:
    """
    Parses a csv file into a list of RentalStay.
    @param fname: path to csv file
    @type fname: str
    @return: list of RentalStay
    @rtype: [RentalStay]
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
    return stays


def sort_by(rows: [dict], col_name: str, rev: bool) -> [dict]:
    """
    Sorts list of dictionaries by the value in a particular key (col_name).
    @param rows: list of dictionaries that share a common key
    @type rows: [dict]
    @param col_name: key to sort by
    @type col_name: str
    @param rev: reverse order
    @type rev: bool
    @return: sorted list of dictionaries
    @rtype: [dict]
    """
    def get_col(row):
        return row[col_name]
    return sorted(rows, key=get_col, reverse=rev)
