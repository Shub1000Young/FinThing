
import csv

def avg_inflation(start,end):
    #count heldur utan um fjolda manuda
    #verd_b heldur utan um raunverdbolgu fyrir hvern manud.
    #medalverdbolga heldur utan um medalverbolgu a timabili.
    count = 0
    verd_b = []
    medalverdbolga = 0
    with open('verdbolga.txt','rb') as verdbolga_skjal:
        verdbolga_skjal = csv.reader(verdbolga_skjal, delimiter='\t')

        for row in verdbolga_skjal:
            if (start==row[0]):# tegar start day byrjar
                verd_b.append(row[1])
                count=count+1# baetir verdbolgu vid shit[]
                for row in verdbolga_skjal:
                    verd_b.append(row[1]) #baetir verdbolgu vid shit[]
                    count=count+1
                    if (end==row[0]):
                        break      # heattir tegar naer end day
                verd_b = map(float,verd_b) #shit var listi med string en convertum yfir i float
                medalverdbolga = (sum(verd_b)/count) # medalverdbolga fra start til end day
                return medalverdbolga


# example 
#x=avg_inflation("2007-12","2019-01")
#print x

