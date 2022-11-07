# s = Stock('GOOG', 100, 490.10)

class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        # !r converts the value to a string
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be integer")
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount
