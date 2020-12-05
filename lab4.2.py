#2

temp1 = float(input("Mata in en temperatur: "))
temp2 = float(input("Mata in en temperatur: "))
temp3 = float(input("Mata in en temperatur: "))
temp4 = float(input("Mata in en temperatur: "))

temp = [temp1, temp2, temp3, temp4]
temp.sort(reverse=True)
print("")
print("Mätningarna i storleksordning:")
print(temp)