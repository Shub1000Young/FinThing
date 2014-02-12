from Loan import *

def loanTest(a, b, c, d, e, time, cash):
	abc = [a, b, c]
	bcd = [b, c, d]
	cde = [c, d, e]
	abcde = [a, b, c, d, e]
	ace = [a, c, e]
	
	loans = [abc, bcd, cde, abcde, ace]
	
	print "Bera saman lánin " + a.name + " , " + b.name + " , " + c.name + " , " + d.name + " , " + e.name + "með því að borga inn " + str(cash) + "krónur í " + str(time) + " mánuði\n"
	for i in range(len(loans)):
		print "fyrir lánin: "
		for j in loans[i]:
			print j.name + " , "
		print "er best að greiða niður:"
		test = evaluate(loans[i], time, cash)
		print test[0] + " þar sem þú græðir " + str(test[1]) + " krónur í vaxtagreiðslur\n"

		
	