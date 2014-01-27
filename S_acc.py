class S_acc:
  'Common base class for all savings accounts'

  def __init__(self, name, principle, i_rate, term, comp_freq):
    'i_rate = APR
     principle = amount deposited
     term = term of loan in months
     '
    self.name = name
    self.principle = principle
    self.i_rate = i_rate/100/12
    self.term = term
    self.balance = self.principle
    
    def pay_in(self, pay_amt):
     CAF = ((1+self.i_rate)**self.term)*self.balance
     FVS = pay_amt*((((1+self.i_rate)**self.term)-1)/self.i_rate)
     self.balance = CAF + FVS 
      