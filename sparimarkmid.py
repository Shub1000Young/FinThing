#coding=UTF-8
import savings

def markmid(total_amount, monthly_amount,i_rate):
    x=0 # fjöldi mán.
    reikningur=savings.savings("reikningur",1,i_rate,0)
    while (reikningur.balance< total_amount):
        reikningur.pay(monthly_amount)
        x=x+1  # heldur utan um fjölda mán. sem tekur að safna upphæðinni

    year=x/12  #finnum árafjölda
    month=x%12  # finnum fjölda mánaða.
    listi= total_amount, monthly_amount,year,month
    return listi