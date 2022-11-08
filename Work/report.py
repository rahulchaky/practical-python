#!/usr/bin/env python
# report.py

# Above is so you can run as a script directly from cmd line
# Ex: python report.py Data/portfolio.csv Data/prices.csv txt

# Using fileparse to read in .csv files
from fileparse import parse_csv
from stock import Stock
import tableformat
from portfolio import Portfolio

# Cleaned up old code
import sys


# Read a stock portfolio file into a list  of dictionaries with keys: name, shares, and price
def read_portfolio(filename, **opts):
    with open(filename) as lines:
        portdicts = parse_csv(
            lines, select=['name', 'shares', 'price'], types=[str, int, float], **opts)

    # portfolio = [Stock(x['name'], x['shares'], x['price']) for x in portfolio_dict]
    # **d takes in a dictionary as args
    portfolio = [Stock(**d) for d in portdicts]
    return Portfolio(portfolio)


def read_prices(filename):
    with open(filename) as lines:
        return parse_csv(lines, types=[str, float], has_headers=False)


# Compute the gain/loss of portfolio by calling above methods
def profit(portfolio, prices):
    oldVal, currVal, currPriceVal, gain = 0, 0, 0, 0

    for stock in portfolio:
        oldVal += int(stock.shares) * float(stock.price)
    for stock in portfolio:
        for name, price in prices:
            if stock.name == name:
                currPriceVal = float(price)
        currVal += int(stock.shares) * currPriceVal

    gain = currVal - oldVal

    print(f"Current Value of Portfolio: ${round(currVal, 2)}")
    print(f"Total Gain/Loss: ${round(gain, 2)}")


# List portfolio
def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        oldVal = float(stock.price)
        currVal = 0
        for name, price in prices:
            if stock.name == name:
                currVal = float(price)
        gain = currVal - oldVal
        report.append((stock.name, int(stock.shares), round(
            currVal, 2), round(gain, 2)))

    return report


def print_report(report, formatter):
    '''
    # Print Report Function
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        format_price = f'${round(price, 2)}'
        print(f'{name:>10s} {shares:>10d} {format_price:>10s} {change:>10.2f}')
    '''

    # Using TableFormatter - did not implement some of the added formatting from prior code
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def portfolio_report(portfolio_filename='Data/portfolio.csv', prices_filename='Data/prices.csv', fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)
    # profit(portfolio, prices) - still functional, just not needed to print everytime


def main(argv):
    if len(argv) == 4:
        portfolio_filename = argv[1]
        prices_filename = argv[2]
        fmt = argv[3]
        portfolio_report(portfolio_filename, prices_filename, fmt)
    else:
        portfolio_report()


# Use this as this will only execute when this specific file is run.
# So when importing this file the whole file won't execute.
if __name__ == '__main__':
    main(sys.argv)

'''
# Outputs Dictionaries better, prolly does other things as well
from pprint import pprint
portfolio = read_portfolio('Data/portfolio.csv')
pprint(portfolio)

prices = read_prices('Data/prices.csv')
pprint(prices)
'''
