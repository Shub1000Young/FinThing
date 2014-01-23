class Loan:
  'Common base class for all loans'

  def __init__(self, name, principle, i_rate, term, comp_freq):
    self.name = name
    self.principle = principle
    self.i_rate = i_rate
    self.comp_freq = comp_freq
    self.tot_loan = (self.principle*(1+(self.i_rate/self.comp_freq)))^(self.term*self.comp_freq)
    self.m_paymnt = (self.tot_loan/self.term)/12
    self.tot_int = self.tot_loan - self.principle
  

    