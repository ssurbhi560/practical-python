# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    '''
    Computes the total cost of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(f)
        for row in f:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares*price
        return total_cost
