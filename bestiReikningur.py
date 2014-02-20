
#coding=UTF-8
import savings
def vaxtatrep(amount, term):

    ############################################ virkar ekki alveg
   #trepreikn=savings.savings("vaxtaþrep",1,3.95,0)   #  reiknar alltaf med 4.25 % voxtum                                  
   
   ## if (5000000 <= trepreikn.balance < 20000000):           #
   ##     interest=4.25                                        #
   ## elif (20000000 <= trepreikn.balance < 75000000):        #
   ##     interest=4.55                                        #
   ## elif (trepreikn.balance >=75000000):                    #
   ##     interest=4.85
   ## trepreikn.pay(amount)  
   balance = 0
   for i in range(1,term):
    if (balance < 5000000):
	interest=3.95
        trepreikn=savings.savings("vaxtaþrep",1,interest,balance)
        trepreikn.pay(amount)
        balance = trepreikn.balance
        #print trepreikn.balance #testing	
    elif (5000000 <= balance < 20000000):           #
        interest=4.25
        trepreikn=savings.savings("vaxtaþrep",1,interest,balance)
        trepreikn.pay(amount)
        balance = trepreikn.balance
        #print trepreikn.balance #testing
    elif (20000000 <= balance < 75000000):        #
        interest=4.55
        trepreikn=savings.savings("vaxtaþrep",1,interest,balance)
        trepreikn.pay(amount)
        balance = trepreikn.balance
        #print trepreikn.balance #testing
    elif (balance >=75000000):                    #
        interest=4.85
        trepreikn=savings.savings("vaxtaþrep",1,interest,balance)
        trepreikn.pay(amount)
        balance = trepreikn.balance
        #print trepreikn.balance # testing
    
    #print trepreikn.i_rate*100*12     #testing
    #print round (trepreikn.balance,0) #testing
  
   return round(trepreikn.balance,0)                       #


def fastvaxtareikningur(amount, term): # aetti ad vera rett
    interest=0
    if (term < 3):
        interest=3.92
        #print "t1" # testing
    if (3 <= term < 6):
        interest=4.91
        #print "t2" # testing
    if (6 <= term < 12):
        interest=5.06
        #print "t3" # testing
    if (term >= 12):
        interest=5.38
        #print "t4" # testing

    fastvaxta=savings.savings("fastvaxtareikningur", term, interest,0)
    fastvaxta.pay(amount)
    #print (round(fastvaxta.balance,0), " F") # testing
    return round(fastvaxta.balance,0)

def vaxtasproti(amount, term):  #aetti ad vera rett
    interest = 3.6
    sprotireikningur=savings.savings("vaxtasproti",term, interest,0)
    sprotireikningur.pay(amount)
    #print (round(sprotireikningur.balance) ," V")#testing
    return round(sprotireikningur.balance)

def calculatesavings(amount, term):
    list=[]
    list.append(vaxtatrep(amount, term))
    list.append(fastvaxtareikningur(amount, term))
    list.append(vaxtasproti(amount, term))
    x = max(list)  # finnum maxid i listanum
    if (list[0]==x):                       #berum saman vid stokin 3 i listanum
        return (list[0],"Vaxtaþrep")        # og finnum nafn reiknings
    elif (list[1]==x):
        return (list[1],"Fastvaxtareikningur")
    elif (list[2]==x):
        return (list[2],"Vaxtasproti")

    
#testing
#x,y = calculatesavings(10000,2)  


