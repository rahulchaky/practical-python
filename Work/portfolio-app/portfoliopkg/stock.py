# stock.py

# s = Stock('GOOG', 100, 490.10)

from .typedproperty import String, Integer, Float


class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    if __debug__:
        name = String('name')
        shares = Integer('shares')
        price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        # !r converts the value to a string
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def cost(self):
        # Return the cost as shares * price
        return self.shares * self.price

    def sell(self, amount):
        # Sell a number of shares and return the remaining number
        self.shares -= amount
