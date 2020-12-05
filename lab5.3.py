#Exempel på kommando prompt

import argparse
import os

parser = argparse.ArgumentParser(description="Allmänn programhjälp")
parser.add_argument("-d", type=str, help="Ange directory:")
parser.add_argument("-f", type=str, help="Ange filter som filerna ska innehålla:")
args = parser.parse_args()

print("Du skrev som -d", args.d)
path = args.d
print("Du skrev som -f", args.f)
namnFilter = args.f

filesInClaes = os.listdir(path)

for filnamn in filesInClaes:
    result = filnamn.endswith('.txt')
    position = filnamn.find(namnFilter)
    if result == True:

        fullPathofFile = path + "\\" + filnamn
        size = os.path.getsize(path + "\\" + filnamn)
        if (size > 100):
            os.remove(fullPathofFile)
        print("")
        print(filnamn, "är", size, "bytes")
