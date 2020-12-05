#1


num1 = int(input("Välj en siffra: "))
num2 = int(input("Välj en siffra: "))
print("")

print("Siffrorna mellan", num1, "och", num2, "är:")
for i in range(num1 + 1, num2):
    print(i, end=', ')


