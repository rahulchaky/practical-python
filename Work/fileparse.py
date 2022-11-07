# fileparse.py
#
# Exercise 3.3
import csv
import sys


def parse_csv(lines, select=None, types=[], has_headers=True, delimiter=",", silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    # Raising an exception
    if select != None and has_headers == False:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    indices = []
    if has_headers:
        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

    records = []
    for rowno, row in enumerate(rows, start=1):
        if not row:     # Skip rows with no data
            continue
        # Filter the row if specific columns were selected
        if indices:
            row = [row[index] for index in indices]

        # Cast type of rows
        if types:
            # To account for missing data
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                # To account for if you want error to not be printed
                if not silence_errors:
                    print(f"Row: {rowno}: Couldn't convert {row}")
                    print(f"Row: {rowno}: {e}")
                else:
                    pass

        if has_headers:
            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)
        else:
            record = tuple(row)
            records.append(record)
    return records
