from avg_inflation import *

class Loan:
  'Common base class for all loans'

  def __init__(self, name, principle, i_rate, term, comp_freq, indexed):

    #principle = Höfuðstóll
	#i_rate = Árlegir Vextir
    #term = lengd láns í mánuðum
	#comp_freq = Hversu oft á ári vextir eru reiknaðir
	#indexed = boolean, verðtrygging

    self.comp_freq = comp_freq
    self.name = name
    self.principle = principle
    self.i_rate = i_rate / 100.0
    self.indexed = indexed
    self.term = term

    if self.indexed: # Bæta við verðtryggingu
        i_rate += avg_inflation("1990-1","2013-1") #Fasti sem verður fall seinna

    self.r = self.i_rate / self.comp_freq #vaxtaprósenta fyrir vaxtatímabil
    self.tot_loan = self.principle*(1.0 + self.r)**(self.comp_freq * (term/12)) # heildar upphæð sem á eftir að borga
    self.m_paymnt = self.tot_loan / self.term # Mánaðarleg greiðsla
    self.tot_int = self.tot_loan - self.principle # Hversu stór hluti heildarlánsins séu vextir
    self.m_int = (((1+self.i_rate/self.comp_freq)**(self.comp_freq/12))-1)*self.principle #hlutfall vaxta næstu greiðslu

#enduukvæmt fall sem keyrir í gegnum mánuðina með yfirgreiðslu og 	endurreiknar vexti hvert sinn
def recalc(loan, t_elapsed, overpay_amt):
	if t_elapsed <= 0: # tíminn búinn, skila
		return [loan.tot_loan, loan.tot_int, loan.principle]
	else: #gera nýtt lán (Python er call by value) og greiða það niður um einn mánuð
		newloan = Loan(loan.name, loan.principle, loan.i_rate, loan.term, loan.comp_freq, loan.indexed)
		principlePayment = loan.m_paymnt - loan.m_int + overpay_amt
		newloan.principle -= principlePayment
		newloan.term -= 1
		return recalc(newloan, t_elapsed-1, overpay_amt)

# Finna besta hagnað fyrir pening og tíma
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

    #return {"nafn" : loans[index].name, "sparnadur" : maxprof - totalSpent, "vextir" : interestprof}

	return [loans[index].name, maxprof - totalSpent, interestprof]
