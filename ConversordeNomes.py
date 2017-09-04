import os
    
TodosFMT = open ("TodosFMT(3314).txt","r")
        
linha = TodosFMT.readline()

for filename in os.listdir("."):

   while filename[1:8] > linha[0:8]:
      linha = TodosFMT.readline()
   if filename.find(linha[0:7])>=0:
      os.rename(filename, "bkp."+filename)


TodosFMT.close()
