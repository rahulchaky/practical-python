# pcost.py
#
# Exercise 1.27

# run as python -i pcost.py to test both portfolio.csv and missing.csv
import csv
import sys


def portfolio_cost(filename):
    cost = 0

    # f = open(filename, 'rt') commented out code blocks are replaced to use the csv import
    f = open(filename)
    rows = csv.reader(f)
    # next(f)  # skips the header
    next(rows)  # skips the header

    for line in f:
        row = line.split(',')
        try:
            # with the csv import we dont need to strip the newline char anymore
            cost += float(row[1]) * float(row[2])
        except ValueError:
            print(f"Failed to parse: {row}")

    f.close()

    return cost


# takes in file from cmd line if provided
# Ex: python pycost.py Data/missing.csv
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total Cost: {round(cost, 2)}")
