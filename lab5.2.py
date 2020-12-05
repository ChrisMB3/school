#2

import os

path = "c:\\kurser\\claes"

filesInClaes = os.listdir(path)

for filnamn in filesInClaes:
    result = filnamn.endswith('.txt')
    if result == True:
        fullPathofFile = path + "\\" + filnamn
        size = os.path.getsize(path + "\\" + filnamn)
        if (size > 100):
            os.remove(fullPathofFile)
        print("")
        print(filnamn, "är", size, "bytes")


#Exempel loggning

# Ta bort alla som INTE är .log i biblioteket claes
# Bossen säger att detta ska köras varje natt kl 02:00
# hmmm ska jag åka till jobbet och köra igång med F5 ???? Tror inte det...?

# TODO
# Skriv i en loggfil (c:\kurser\executionlog.txt) vilka filer som tagits bort
#               2020-08-31 12:11:12 Filen blabla.txt togs bort

#print("Superduper File Remover v1.0 (C) Stefan")
#path = "c:\\kurser\\claes"

#filesInClaes = os.listdir( path )

#for filNamn in filesInClaes:
   #result = filNamn.endswith('.log')
   #if result == False:
        #os.remove(path + "\\" + filNamn)
        #f = open("c:\\kurser\\executionlog.txt", "a")
        #datetime_object = datetime.datetime.now()
        #f.write(f"{datetime_object} Filen {filNamn} togs bort\n")
        #f.close()