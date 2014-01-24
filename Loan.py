class Loan:
  'Common base class for all loans'

  def __init__(self, name, principle, i_rate, term, comp_freq):
    'i_rate = interest rate as decimal
     principle = amount borrowed
     term = term of loan in years
     comp_freq = frequency of interest compounding per year
     '
    self.name = name
    self.principle = principle
    self.i_rate = i_rate
    self.comp_freq = comp_freq
    self.tot_loan = (self.principle*(1+(self.i_rate/self.comp_freq)))**(self.term*self.comp_freq)
    self.m_paymnt = (self.tot_loan/self.term)/12
    self.tot_int = self.tot_loan - self.principle
    self.m_int = (self.tot_int/self.term)/12
    
  def recalc(self, t_elapsed):
    self.principal = self.principal-((t_elapsed*self.m_paymnt)-(t_elapsed*self.m_int))
    self.term = self.term-(t_elapsed/12)
    
  
  

    