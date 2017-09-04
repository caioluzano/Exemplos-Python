import os
    
##FMT = "C:\Users\caio.luzano\Desktop\Raizen\TodosFMT(3314).txt"
##TFMT = open (FMT,"r")
##
##
##Todas = open ("C:\Users\caio.luzano\Desktop\Raizen\Todos (3314).txt","r")
###gerar = open (lido+".cnf","w")
##i = 0
##j = 0
##tem = 0
##
##for linha in Todas:
##    i=i+1
##    for flinha in TFMT:
##        #print flinha[0:7]
##        if linha[1:8] == flinha[0:7]:
##            print i
##            tem = 1
##            break
##    TFMT.close()
##    TFMT = open (FMT,"r")
##    if  tem != 1:
##        #print flinha
##        print linha[1:8]
##        print "deu ruim -----------------------------------------------"
##        break
##    tem = 0
##    #print "------------------------------------"+linha


Todas = open ("C:\Users\caio.luzano\Desktop\Raizen\TodosFMT(3314).txt","r")
Todas2 = open ("C:\Users\caio.luzano\Desktop\Raizen\TodosFMT(3314).txt","r")
i=0
rep = 0

linha2 =  Todas2.readline()

for linha1 in Todas:

    linha2 =  Todas2.readline()
    print linha1
    print linha2
    if linha1 == linha2:
        rep = rep + 1

print rep

Todas.close()
Todas2.close()
