#!/usr/bin/env python
# pcost.py

# Above is so you can run as a script
# Ex: python pcost.py Data/portfolio.csv

# Updating to use report.py
from . import report

# run as python -i pcost.py to test both portfolio.csv and missing.csv
import sys


def portfolio_cost(filename):
    # Computes the total cost (shares * price) of a portfolio file
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost


def main(argv):
    # takes in file from cmd line if provided
    # Ex: python pycost.py Data/missing.csv
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'
        # filename = 'Data/missing.csv'
        # filename = 'Data/portfoliodate.csv'

    cost = portfolio_cost(filename)
    print(f"Total Cost: ${round(cost, 2)}")


if __name__ == '__main__':
    import sys
    main(sys.argv)
