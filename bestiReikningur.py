
#coding=UTF-8
import savings
def vaxtatrep(amount, term):
    intrest=3.95  ############################################ virkar ekki alveg
    trepreikn=savings.savings("vaxtaþrep",term,intrest,0)   #  reiknar alltaf med 4.25 % voxtum
                                                            # nema nu tegar se heill hellingur inna reikn..
    if (5000000 <= trepreikn.balance < 20000000):           #
        intrest=4.25                                        #
    elif (20000000 <= trepreikn.balance < 75000000):        #
        intrest=4.55                                        #
    elif (trepreikn.balance >=75000000):                    #
        intrest=4.85
    trepreikn.pay(amount)                                    #
                                                            #
    return round(trepreikn.balance,0)                       #
####################################################################### 

def fastvaxtareikningur(amount, term): # aetti ad vera rett
    intrest=0
    if (term < 3):
        intrest=3.92
    if (3 <= term < 6):
        intrest=4.91
    if (6 <= term < 12):
        intrest=5.06
    if (term >= 12):
        intrest=5.38

    fastvaxta=savings.savings("fastvaxtareikningur", term, intrest,0)
    fastvaxta.pay(amount)
    return round(fastvaxta.balance,0)

def vaxtasproti(amount, term):  #aetti ad vera rett
    intrest = 3.6
    sprotireikningur=savings.savings("vaxtasproti",term, intrest,0)
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

