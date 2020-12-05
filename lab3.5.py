#5


sum = 0
list = []

while True:
    tal = int(input("Mata in ett tal: "))
    if tal == 0:
        break
    print("Du matade in tal:", tal)

    sum = (sum + tal)
    print("")
    print("Summan av alla tal är", sum)

    list.insert(0, tal)
    lenCount = len(list)
    if lenCount > 3:
        lenCount = 3
    sumMedel = 0

    antalTillagda = 0
    for i in list:
        sumMedel = sumMedel + i
        antalTillagda = antalTillagda + 1
        if antalTillagda == lenCount:
            break
    print("Medlevärde på de", lenCount, "senaste är,", (antalTillagda/lenCount))