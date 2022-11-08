# ticker.py

# python ticker.py Data/portfolio.csv Data/stocklog.csv txt

import csv
import sys

from follow import follow
import report
import tableformat


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def ticker(portfile='Data/portfolio.csv', logfile='Data/stocklog.csv', fmt='txt'):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)

    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row(
            [row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"])


def main(argv):
    if len(argv) != 4:
        ticker()
    else:
        ticker(argv[1], argv[2], argv[3])


if __name__ == '__main__':
    main(sys.argv)
