#1

num1 = int(input("Mata in ett tal: "))
num2 = int(input("Mata in ett tal: "))
num3 = int(input("Mata in ett tal: "))
num4 = int(input("Mata in ett tal: "))

lista = [num1, num2, num3, num4]
lista.sort(reverse= True)
print("")
print("Talen i storleksordning:")
print(lista)