#2


while True:
    num1 = int(input("Välj ett tal: "))
    num2 = int(input("Välj ett tal: "))

    print("")
    print("Summan av talen är:", num1 + num2)
    print("")

    if input("Vill du fortsätta ja/nej? ").lower() != "ja":
        break
