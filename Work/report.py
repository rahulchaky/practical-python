# Using fileparse to read in .csv files
from fileparse import parse_csv

# Cleaned up old code
import csv
import sys

# Outputs Dictionaries better, prolly does other things as well
from pprint import pprint


# Read a stock portfolio file into a list  of dictionaries with keys: name, shares, and price
def read_portfolio(filename):
    return parse_csv(filename)


def read_prices(filename):
    return parse_csv(filename, has_headers=False)


# Compute the gain/loss of portfolio by calling above methods
def profit(portfolio, prices):
    oldVal, currVal, currPriceVal, gain = 0, 0, 0, 0

    for stock in portfolio:
        oldVal += int(stock['shares']) * float(stock['price'])
    for stock in portfolio:
        for name, price in prices:
            if stock['name'] == name:
                currPriceVal = float(price)
        currVal += int(stock['shares']) * currPriceVal

    gain = currVal - oldVal

    print(f"Current Value of Portfolio: ${round(currVal, 2)}")
    print(f"Total Gain/Loss: ${round(gain, 2)}")


# List portfolio
def make_report(portfolio, prices):
    report = []

    for stock in portfolio:
        oldVal = float(stock['price'])
        currVal = 0
        for name, price in prices:
            if stock['name'] == name:
                currVal = float(price)
        # currVal = float(prices[stock['name']])
        gain = currVal - oldVal
        report.append((stock['name'], int(stock['shares']), round(
            currVal, 2), round(gain, 2)))

    return report


def print_report(report):
    # Print Report Function
    # 2.3 Formatting
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(
        f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        format_price = f'${round(price, 2)}'
        print(f'{name:>10s} {shares:>10d} {format_price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename='Data/portfolio.csv', prices_filename='Data/prices.csv'):
    # Function to call other functions
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)
    profit(portfolio, prices)


# Use this as this will only execute when this specific file is run.
# So when importing this file the whole file won't execute.
if __name__ == '__main__':
    if len(sys.argv) == 3:
        portfolio_filename = sys.argv[1]
        prices_filename = sys.argv[2]
        portfolio_report(portfolio_filename, prices_filename)
    else:
        portfolio_report()

'''
Various things to try running
portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')

files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
for name in files:
    print(f'{name:-^43s}')
    portfolio_report(name, 'Data/prices.csv')
    print()
'''
# portfolio = read_portfolio('Data/portfolio.csv')
# pprint(portfolio)

# prices = read_prices('Data/prices.csv')
# pprint(prices)
