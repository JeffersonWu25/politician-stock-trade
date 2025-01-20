""" Class definition for portfolio """

class Portfolio:

    holdings = {}

    def __init__(self) -> None:
        """ default constructor"""
        self.holdings = {}

    def update_holdings(self, stock, amount):
        """ returns true if holdings is modified"""
        if amount > 0:
            # buy for first time
            if stock not in self.holdings:
                self.holdings[stock] = amount
                return True
            
            # normal buy
            self.holdings[stock] += amount
            return True
        else:
            # sell before buy
            if stock not in self.holdings:
                return False
            
            # sell all
            if -amount >= self.holdings[stock]:
                del self.holdings[stock]
                return True
            
            # normal sell
            self.holdings[stock] += amount
            return True
    
    def get_holdings(self):
        return self.holdings