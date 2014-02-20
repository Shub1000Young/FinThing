#coding=UTF-8
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

    #if self.indexed: # Bæta við verðtryggingu
    #    self.i_rate += avg_inflation("1990-01","2013-01") #Fasti sem verður fall seinna

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
	totalTime = months
	intermedLoans = [] #millibreyta ef að best er að greiða fyrst eitt lán svo annað
	newtotal = 0 #millibreyta með heildarsparnað núverandi láns
	maxprof = 0 #mesti sparnaður
	index = 0	# númer láns sem á að greiða niður
	#hér athugum við lán sem eru styttri en sparnaðartímabilið okkar
	for i in range(len(loans)):
		if loans[i].term <= months:
			intermaxprof = 0
			interintex = 0
			intermonths = loans[i].term-1
			for j in range(len(loans)):
				newtotal = recalc(loans[j], intermonths, amount)
				if newtotal > intermaxprof:
					intermaxprof = newtotal
					interindex = j
			if interindex == i: #ef stutta lánið er best á þessum tíma
				intermedLoans.append([loans[i], intermaxprof])
				totalTime -= (loans[i].term -1)
			loans.pop(i)

	#skoðar öll lán sem eru stærri en spartímabilið okkar
	for i in range(len(loans)):
		newtotal= recalc(loans[i], totalTime, amount)
		if newtotal > maxprof:
			maxprof = newtotal
			index = i

	if len(intermedLoans) != 0:
		if len(loans) != 0:
			return [intermedLoans, loans[index].name, maxprof]
		else :
			return [intermedLoans, totalTime]

	return [loans[index], maxprof]

#þetta fall skilar tveimur listum af mánaðarlegum eftirstöðvum fyrir línurit
def overview(loan, t_elapsed, overpay_amt):
	overpayTime = t_elapsed
	original = [] # eftistöðvar með engum yfirgreiðslum
	newlist = [] # eftirstöðvar með yfirgreiðslum
	loanA = Loan("loan1", loan.principle, loan.i_rate*100.0, loan.term, loan.comp_freq, loan.indexed)#Nýtt lán byggt á láni
	for i in range(loan.term-1): #borgar niður lán og bætir eftirstöðvum í lista
		loanB = Loan("loanB", loanA.principle, loanA.i_rate*100.0, loanA.term, loanA.comp_freq, loanA.indexed)#Nýtt lán byggt á loanA
		original.append(int(loanB.principle))
		principlePayment = loanA.m_paymnt - loanA.m_int
		loanB.principle -= principlePayment #greiða niður höfuðstól
		loanB.term -= 1 # minka tímabil
		loanA = Loan("loanA", loanB.principle, loanB.i_rate*100.0, loanB.term, loanB.comp_freq, loanB.indexed) #LoanA er nýja lánið
	original.append(0)
	loanA = Loan("loan1", loan.principle, loan.i_rate*100.0, loan.term, loan.comp_freq, loan.indexed)#Nýtt lán byggt á láni
	for i in range(loan.term-1):#listi af eftirstöðvum með yfirborgunum
		loanB = Loan("loanB", loanA.principle, loanA.i_rate*100.0, loanA.term, loanA.comp_freq, loanA.indexed)#Nýtt lán byggt á loanA
		newlist.append(int(loanB.principle))
		if overpayTime > 0:
			principlePayment = loanA.m_paymnt - loanA.m_int + overpay_amt
			overpayTime -=1
		else:
			principlePayment = loanA.m_paymnt - loanA.m_int
		loanB.principle -= principlePayment #greiða niður höfuðstól
		loanB.term -= 1 # minka tímabil
		loanA = Loan("loanA", loanB.principle, loanB.i_rate*100.0, loanB.term, loanB.comp_freq, loanB.indexed) #LoanA er nýja lánið
	newlist.append(0)
	return [original, newlist]