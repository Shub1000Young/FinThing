class savings:
    def __init__(self, name, term, i_rate, balance):
        self.name = name
        self.i_rate = i_rate/100.0/12.0
        self.term = term
        self.balance = balance

    def pay(self, amount):
        CAF = ((1+self.i_rate)**self.term)*self.balance
        FVS = amount*((((1+self.i_rate)** self.term)-1)/self.i_rate)
        self.balance = CAF + FVS