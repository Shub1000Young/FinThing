
#coding=UTF-8
import savings
def vaxtatrep(amount, term):
   interest=3.95  ############################################ virkar ekki alveg
   trepreikn=savings.savings("vaxtaþrep",1,interest,0)   #  reiknar alltaf med 4.25 % voxtum
                                                            # nema nu tegar se heill hellingur inna reikn..
   ## if (5000000 <= trepreikn.balance < 20000000):           #
   ##     interest=4.25                                        #
   ## elif (20000000 <= trepreikn.balance < 75000000):        #
   ##     interest=4.55                                        #
   ## elif (trepreikn.balance >=75000000):                    #
   ##     interest=4.85
   ## trepreikn.pay(amount)                                    #
   for i in range (1,term)
    if (5000000 <= trepreikn.balance < 20000000):           #
        interest=4.25                                        #
    elif (20000000 <= trepreikn.balance < 75000000):        #
        interest=4.55                                        #
    elif (trepreikn.balance >=75000000):                    #
        interest=4.85
    
    trepriekn.pay(amount/term)
  
   return round(trepreikn.balance,0)                       #
####################################################################### 

def fastvaxtareikningur(amount, term): # aetti ad vera rett
    interest=0
    if (term < 3):
        interest=3.92
    if (3 <= term < 6):
        interest=4.91
    if (6 <= term < 12):
        interest=5.06
    if (term >= 12):
        interest=5.38

    fastvaxta=savings.savings("fastvaxtareikningur", term, interest,0)
    fastvaxta.pay(amount)
    return round(fastvaxta.balance,0)

def vaxtasproti(amount, term):  #aetti ad vera rett
    interest = 3.6
    sprotireikningur=savings.savings("vaxtasproti",term, interest,0)
    sprotireikningur.pay(amount)
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

#daemi um notkun
#x,y = calculatesavings(10000,12)
#print x,y

