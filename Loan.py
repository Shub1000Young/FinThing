class Loan:
  'Common base class for all loans'

  def __init__(self, name, principle, i_rate, term, comp_freq):
    'i_rate = annual interest rate as percentage
     principle = amount borrowed
     term = term of loan in years
     '
    self.name = name
    self.principle = principle
    self.i_rate = i_rate
    self.term = term
    self.r = (self.i_rate/1200)
    self.m_paymnt = (self.principal*self.r)*(1+self.r)**self.term
    self.tot_loan = self.m_paymnt* self.term
    self.tot_int = self.tot_loan - self.principle
    self.m_int = (self.tot_int/self.term)
    
  def recalc(self, t_elapsed, overpay_amt):
    self.principal = self.principal-((t_elapsed*self.m_paymnt)-(t_elapsed*self.m_int))- overpay_amt
    self.term = self.term-t_elapsed
    
  
  

    