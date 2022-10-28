# report.py
#
# Exercise 2.4

import csv
import sys

# Outputs Dictionaries better, prolly does other things as well
from pprint import pprint

'''
# Takes in the portfolio and reads it into a list with each item as a tuple
def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # stores the column names of the csv file

        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)

        return portfolio
'''


def read_portfolio(filename):
    # Takes in the portfolio and reads it into a list with each item as a dict
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # stores the column names of the csv file

        for row in rows:
            holding = {'name': row[0], 'shares': int(
                row[1]), 'price': float(row[2])}
            portfolio.append(holding)

        return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # headers = next(rows) # there is no header in prices file

        for row in rows:
            try:
                prices[row[0]] = row[1]
            except IndexError:
                pass  # this makes it so the program does nothing

            # print(row)

        return prices


# Compute the gain/loss of portfolio by calling above methods
def profit(portfolio, prices):
    oldVal, currVal, gain = 0, 0, 0

    for stock in portfolio:
        oldVal += int(stock['shares']) * float(stock['price'])
    for stock in portfolio:
        currVal += int(stock['shares']) * float(prices[stock['name']])

    gain = currVal - oldVal

    print(f"Current Value of Portfolio: {round(currVal, 2)}")
    print(f"Total Gain/Loss: {round(gain, 2)}")


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
profit(portfolio, prices)
'''
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
'''
# portfolio = read_portfolio('Data/portfolio.csv')
# pprint(portfolio)

# prices = read_prices('Data/prices.csv')
# pprint(prices)
