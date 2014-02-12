#coding=UTF-8
import unittest
from Loan import *

class testLoanFunctions(unittest.TestCase):
    def test_evaluate(self):
        good = Loan("Good", 40000000, 4, 240, 12, False)
        bad = Loan("Bad", 3000000, 5, 90, 12, False)
        worst = Loan("Kúlulán", 4000000, 4, 48, 12, False)

        self.assertTrue(evaluate([good, bad], 5, 10000)[0] == good.name)
        self.assertTrue(evaluate([bad, worst], 5, 10000)[0] == bad.name)
        self.assertFalse(evaluate([good, worst], 5, 10000)[0] == worst.name)

    def test_properties(self):
        testLoan1 = Loan("Lanlan", 4000000, 5, 240, 12, False)
        testLoan2 = Loan("Lanlan", 10000000, 3, 360, 12, False)

        #Loan2
        self.assertTrue(6335500 < testLoan1.tot_loan < 6335600)
        self.assertTrue(2335500 < testLoan1.tot_int < 2335600)

        #Loan2
        self.assertTrue(15177700 < testLoan2.tot_loan < 15177800)
        self.assertTrue(5177700 < testLoan2.tot_int < 5177800)

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)