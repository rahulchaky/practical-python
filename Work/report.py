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


# Read a stock portfolio file into a list  of dictionaries with keys: name, shares, and price
def read_portfolio(filename):
    # Takes in the portfolio and reads it into a list with each item as a dict
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # stores the column names of the csv file
        '''
        for row in rows:
            holding = {'name': row[0], 'shares': int(
                row[1]), 'price': float(row[2])}
            portfolio.append(holding)
        '''
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)

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


# List portfolio
def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        oldVal = float(stock['price'])
        currVal = float(prices[stock['name']])
        gain = currVal - oldVal
        report.append((stock['name'], int(stock['shares']), round(
            float(prices[stock['name']]), 2), round(gain, 2)))

    return report


# portfolio = read_portfolio('Data/portfolio.csv')
portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')

report = make_report(portfolio, prices)
# for r in report:
# print(r)
# print('%10s %10d %10.2f %10.2f' % r)

# 2.3 Formatting
headers = ('Name', 'Shares', 'Price', 'Change')
print(
    f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    format_price = f'${round(price, 2)}'
    print(f'{name:>10s} {shares:>10d} {format_price:>10s} {change:>10.2f}')


# profit(portfolio, prices)
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
