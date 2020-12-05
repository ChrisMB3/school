#2

a = int(input("Hur många paket mjölk finns det kvar? "))

if a < 10:
    print("Beställ 30 nya paket")

elif a > 20:
    print("Du behöver inte beställa några nya paket")

else:
    print("Beställ 20 nya paket")