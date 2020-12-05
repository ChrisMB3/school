#Simple dice program that detects if the dice gets the value 1 and rolls it again.

import random   #imports random number generator used for dice

def RollTheDice(Rolls):     #function where the dice is rolled
    DiceRolls = []

    for g in range(0, Rolls):
        number = random.randint(1, 6)
        DiceRolls += [number]
    return DiceRolls

def List(a):        #function where the dices with result "one" gets deleted
    x = 1
    q = len(a)
    t = 0
    for j in a:
        if j == 1:
            while t < 2:
                i = 0
                f = 0
                for o in a:
                    if o == 1:
                        t = 0
                        while f < q:
                            if i <= len(a):
                                g = a[i]
                                if g == 1:
                                    r = a.pop(i)
                                    i -= 1
                                    z = RollTheDice(2)
                                    f += 1
                                    a += z
                                    print("Tärning", x, "blev 1 och kastades därför om två gånger.")
                                    x -= 1
                                i += 1
                                x += 1
                            f += 1

                t += 1
    return a

def PrintRolls(b):      #function to print the results of the dice rolling
    Sum = sum(b)
    for number in b:
        print("-----")
        print("--" + str(number) + "--")
        print("-----")
        print()
    return Sum

def Options():      #the core of the code which gives the player vital information and delegates to the rest of the function
    print("| Albin Lundin " + "| 19990423-6578 " + "| 2020-04-25 |")
    i = 0
    ToltalSum = 0
    NumberOfRolls = 0
    while i < 1:
        print()
        print("[1]" + " Slå en tärning")
        print("[2]" + " Slå flera tärningar")
        print("------------------------")
        print("[3]" + " Avsluta program")
        print()
        try:
            choice = int(input("Skriv ditt val här: "))
            if choice == 1:
                a = RollTheDice(1)
                b = List(a)
                c = PrintRolls(b)
                ToltalSum += sum(b)
                NumberOfRolls += len(b)
                print("Summa detta kast:", c)
            elif choice == 2:
                j = 0
                while j < 1:
                    try:
                        Rolls = int(input("Hur många tärningar? "))
                        if 1 <= Rolls <= 4:
                            a = RollTheDice(Rolls)
                            b = List(a)
                            c = PrintRolls(b)
                            print("Summa detta kast:", c)
                            ToltalSum += sum(b)
                            NumberOfRolls += len(b)
                            j = 1
                        else:
                            print("Skriv en siffra mellan 1 och 4.")
                    except:
                        print("Skriv en siffra mellan 1 och 4.")
            elif choice == 3:
                print("Den totala summan blev: ", ToltalSum)
                print("Totalt antal slagna tärningar: ", NumberOfRolls, "st")
                k = 0
                while k < 1:
                    f = input("Vill du att spela igen? ").upper()
                    if f == "JA":
                        ToltalSum = 0
                        NumberOfRolls = 0
                        i = 0
                        k = 1
                    elif f == "NEJ":
                        i = 1
                        k = 1
                    else:
                        print("Svara ja eller nej ")
            else:
                print("------------------------------------------------------------------------")
                print("Angivet värde är felaktigt. Vänligen välj mellan alternativ 1, 2 eller 3.")
                print("------------------------------------------------------------------------")
        except:
            print("------------------------------------------------------------------------")
            print("Angivet värde är felaktigt. Vänligen välj mellan alternativ 1, 2 eller 3.")
            print("------------------------------------------------------------------------")

def main():     #main function
    Options()

main()      #calling the main function
