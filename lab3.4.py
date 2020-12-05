#4

sum = 0
while True:
    tal = int(input("Mata in ett tal: "))
    if tal == 0:
        break

    print("Du matade in tal:", tal)

    sum = (sum + tal)
    print("")
    print("Summan av alla tal är", sum)
