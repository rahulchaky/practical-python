# pcost.py
#
# Exercise 1.27

# Updating to use report.py
from report import read_portfolio

# run as python -i pcost.py to test both portfolio.csv and missing.csv
import csv
import sys


def portfolio_cost(filename):
    records = read_portfolio(filename)

    # Computes the total cost (share * price) of a portfolio file
    total_cost = 0.0
    # Adding Enumerate + Try-Except (2.4)
    for rowno, row in enumerate(records, start=1):
        try:
            nshares = int(row['shares'])
            price = float(row['price'])
            total_cost += nshares * price
        # This catches errors in int() and float() conversions above
        except ValueError:
            print(f'Row {rowno}: Bad row: {row}')

    return total_cost


# takes in file from cmd line if provided
# Ex: python pycost.py Data/missing.csv
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
    # filename = 'Data/missing.csv'
    # filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print(f"Total Cost: {round(cost, 2)}")
