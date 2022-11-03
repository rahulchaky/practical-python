# pcost.py
#
# Exercise 1.27

# run as python -i pcost.py to test both portfolio.csv and missing.csv
import csv
import sys


def portfolio_cost(filename):
    # Computes the total cost (share * price) of a portfolio file
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # stores the column names of the csv file
        '''
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price

        return total_cost
        '''
        # Adding Enumerate + Try-Except (2.4)
        for rowno, row in enumerate(rows, start=1):
            # Using headers
            record = dict(zip(headers, row))
            # record >>> {'price' : xx.xx, 'name' : 'AA', 'shares' : xxx, ...}
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')

        return total_cost

    '''
    OLD CODE

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
    '''


# takes in file from cmd line if provided
# Ex: python pycost.py Data/missing.csv
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    # filename = 'Data/portfolio.csv'
    # filename = 'Data/missing.csv'
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)
print(f"Total Cost: {round(cost, 2)}")
