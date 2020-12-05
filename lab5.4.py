#4


import datetime

antal = int(input("Hur många datum vill du logga?:"))

file = open('c:\\kurser\\claes\\test.txt', 'a')
for i in range(0, antal):

    file.write(f"{datetime.datetime.now()}\n")
file.close()