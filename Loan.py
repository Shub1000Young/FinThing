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
    self.tot_loan = (((self.r)*self.principle)/(1-(1+(self.r))**-self.term))*self.term # heildar upphæð sem á eftir að borga
    self.m_paymnt = self.tot_loan / self.term # Mánaðarleg greiðsla
    self.tot_int = self.tot_loan - self.principle # Hversu stór hluti heildarlánsins séu vextir
    self.m_int = (((1+self.i_rate/self.comp_freq)**(self.comp_freq/12))-1)*self.principle #hlutfall vaxta næstu greiðslu


#lúppa sem fer í gegnum lánið, greiðir niður og reiknar vexti
def recalc(loan, t_elapsed, overpay_amt):
	tot_intP = 0 # heildargreiddir vextir
	loanA = Loan("loan1", loan.principle, loan.i_rate*100.0, loan.term, loan.comp_freq, loan.indexed)#Nýtt lán byggt á láni
	for i in range(t_elapsed):
		loanB = Loan("loanB", loanA.principle, loanA.i_rate*100.0, loanA.term, loanA.comp_freq, loanA.indexed)#Nýtt lán byggt á loanA
		principlePayment = loanA.m_paymnt - loanA.m_int + overpay_amt #Greiðsla af höfuðstól
		tot_intP += loanA.m_int #heildar vextir greiddir
		loanB.principle -= principlePayment #greiða niður höfuðstól
		loanB.term -= 1 # minka tímabil
		loanA = Loan("loanA", loanB.principle, loanB.i_rate*100.0, loanB.term, loanB.comp_freq, loanB.indexed) #LoanA er nýja lánið
	return (loan.tot_int - loanA.tot_int - tot_intP) #skila heildar vaxtasparanaði
	
	
# Finna besta hagnað fyrir pening og tíma
def evaluate(loans, months, amount):
	totalSpent = months * amount
	newtotal = []
	maxprof = 0
	index = 0
	for i in range(len(loans)):
		newtotal= recalc(loans[i], months, amount)
		if newtotal > maxprof:
			maxprof = newtotal
			index = i

    #return {"nafn" : loans[index].name, "sparnadur" : maxprof - totalSpent, "vextir" : interestprof}

	return [loans[index].name, maxprof, maxprof]
