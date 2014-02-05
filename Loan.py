class Loan:
  'Common base class for all loans'

  def __init__(self, name, principle, i_rate, term, comp_freq, indexed):
    
    #principle = amount borrowed
	#i_rate = annual interest rate as percentage
    #term = term of loan in months
	#comp_freq = how ofter per year interest is compounded
	#indexed = boolean, true if loan is indexed
	
    self.comp_freq = comp_freq 
    self.name = name
    self.principle = principle
    self.i_rate = i_rate / 100.0
	if indexed: # add price index as a monthly interest
		i_rate += 0.04 #placeholder for indexed constant function
    self.term = term
    self.r = self.i_rate / self.comp_freq #compound interest rarte
    self.tot_loan = self.principle*(1.0 + self.r)**(self.comp_freq * (term/12)) # total loan
    self.m_paymnt = self.tot_loan / self.term # montly payment
    self.tot_int = self.tot_loan - self.principle # amount of total loan that is interest
    self.m_int = (((1+self.i_rate/self.comp_freq)**(self.comp_freq/12))-1)*self.principle #interest due this month
    
def recalc(loan, t_elapsed, overpay_amt):
	if t_elapsed <= 0:
		return [loan.tot_loan, loan.tot_int, loan.principle]
	else:
		newloan = Loan(loan.name, loan.principle, loan.i_rate, loan.term, loan.comp_freq, loan.indexed)
		principlePayment = loan.m_paymnt - loan.m_int + overpay_amt #hversu mikið fer af höfuðstól
		newloan.principle -= principlePayment
		newloan.term -= 1
		return recalc(newloan, t_elapsed-1, overpay_amt)
	
def evaluate(loans, months, amount):
	totalSpent = months * amount
	newtotal = []
	maxprof = 0
	index = 0
	interestprof = 0
	for i in range(len(loans)):
		newtotal= recalc(loans[i], months, amount)
		if loans[i].tot_loan - newtotal[0] > maxprof:
			maxprof = loans[i].tot_loan - newtotal[0]
			index = i
			interestprof = loans[i].tot_int - newtotal[1]
	return {"nafn" : loans[index].name, "sparnadur" : maxprof - totalSpent, "vextir" : interestprof}