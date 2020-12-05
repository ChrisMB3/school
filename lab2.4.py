#4

age = 0
while age == False:
    try:
        age = int(input("Skriv in din ålder: "))
        var = age == False

    except:
        print("Vänligen skriv in en siffra")

if age < 18:
    print("Du är inte myndig")

elif age > 65:
    print("Du är pensionär")

else:
    print("Du är myndig men inte pensionär")
