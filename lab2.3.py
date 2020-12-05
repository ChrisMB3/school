#3


temp = float(input("Mata in din temperatur: "))

if temp > 37.8:
    print("Du har feber")

    if temp > 39.5:
        print("och bör uppsöka läkare")

else:
    print("Du har inte feber")