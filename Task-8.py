class MoneyFmt:

    def __init__(self, dengi):
        self.cash = dengi
        self.dollarize()
                

    def update(self, dengi):
        self.cash = dengi
        self.dollarize()
        
    def repr(self):
        self.float_cash = float(self.cash)

    def str(self):
        self.str_cash = str(self.cash)

    def dollarize(self):
        if self.cash >= 0:
            print('${:,.2f}'.format(self.cash))
        else:
            print('-${:,.2f}'.format(self.cash))

go = MoneyFmt(123456789.12345)

go.update(98765432.98765432)

