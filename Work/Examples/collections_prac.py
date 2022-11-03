# Collections Module
from collections import Counter

# Copied from report.py
import csv


# Read a stock portfolio file into a list  of dictionaries with keys: name, shares, and price
def read_portfolio(filename):
    # Takes in the portfolio and reads it into a list with each item as a dict
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # stores the column names of the csv file

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }
            portfolio.append(stock)

    return portfolio


def counter_init(portfolio):
    # Fill counter with data
    for s in portfolio:
        holdings[s['name']] += s['shares']
    return holdings


def total_shares(holdings):
    # Tabulate total number of shares of each stock
    print(holdings)


def indiv_values(holdings, name):
    print(holdings[name])


def most_held(holdings, amount):
    # Get n-number of most held stocks
    print(holdings.most_common(amount))


def combine(holdings, holdings2):
    # Combining porfolios
    combined = holdings + holdings2
    print(combined)


# Read in portfolios
portfolio = read_portfolio('Data/portfolio.csv')
portfolio2 = read_portfolio('Data/portfolio2.csv')
# Using Counter objects
holdings = Counter()
holdings = counter_init(portfolio)
holdings2 = counter_init(portfolio2)

# Calling functions
total_shares(holdings)
total_shares(holdings2)
indiv_values(holdings, 'IBM')
indiv_values(holdings, 'MSFT')
most_held(holdings, 3)
combine(holdings, holdings2)

# Can repurpose so that the print statements are return statements instead
