from Loan import *

def loanTest(a, b, c, d, e, time, cash):
	abc = [a, b, c]
	bcd = [b, c, d]
	cde = [c, d, e]
	abcde = [a, b, c, d, e]
	ace = [a, c, e]
	
	loans = [abc, bcd, cde, abcde, ace]
	
	print "Bera saman l�nin " + a.name + " , " + b.name + " , " + c.name + " , " + d.name + " , " + e.name + "me� �v� a� borga inn " + str(cash) + "kr�nur � " + str(time) + " m�nu�i\n"
	for i in range(len(loans)):
		print "fyrir l�nin: "
		for j in loans[i]:
			print j.name + " , "
		print "er best a� grei�a ni�ur:"
		test = evaluate(loans[i], time, cash)
		print test[0] + " �ar sem �� gr��ir " + str(test[1]) + " kr�nur � vaxtagrei�slur\n"

		
	