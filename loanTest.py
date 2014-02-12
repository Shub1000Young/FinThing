from Loan import *

def loanTest(a, b, c, d, e, time, cash):
	abc = [a, b, c]
	bcd = [b, c, d]
	cde = [c, d, e]
	abcde = [a, b, c, d, e]
	ace = [a, c, e]
	
	loans = [abc, bcd, cde, abcde, ace]
	
	print "Bera saman lánin " + a.name + " , " + b.name + " , " + c.name + " , " + d.name + " , " + e.name + "með því að borga inn" + str(cash) + "krónur í " + str(time) + " mánuði\n"
	for i in range(len(loans)):
		print "fyrir lánin: "
		for j in loans[i]:
			print j.name + " , "
		print "er best að greiða niður:"
		test = evaluate(loans[i], time, cash)
		print test[0] + " þar sem þú græðir " + str(test[1]) + " krónur í vaxtagreiðslur\n"

		
loan1 = Loan("húsnæðislán", 40000000, 4, 240, 12, False)
loan2 = Loan("Bílalán", 3000000, 5, 90, 12, False)
loan3 = Loan("Yfirdráttur", 500000, 15, 6, 12, False)
loan4 = Loan("Kúlulán", 4000000, 4, 48, 12, False)
loan5 = Loan("Námslán", 80000000, 2.3, 100, 12, False)
loanTest(loan1, loan2, loan3, loan4, loan5, 5, 10000)

