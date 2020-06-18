
import csv
# Exercise 2.4
def read_portfolio(filename):
    ''' reads the data of file into list of tuples and dictionaries'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            #holding = (row[0], int(row[1]), float(row[2]))
            stock = {
                        'name':row[0],
                        'shares': int(row[1]),
                        'price': float(row[2]) 
                    }
            portfolio.append(stock)
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)


def read_prices(filename):
    '''
    reads the content of file in dictionaries
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices

prices = read_prices('Data/prices.csv')
print(prices)