#3

name1 = input("Skriv ett namn här: ").lower()
que1 = input("Vill du fortsätta: ")
if que1 == "j":
    name2 = input("Skriv ett namn här: ").lower()
    que2 = input("Vill du fortsätta: ")

    if que2 == "j":
        name3 = input("Skriv ett namn här: ").lower()
        que3 = input("Vill du fortsätta: ")

        if que3 == "j":
            name4 = input("Skriv ett namn här: ").lower()
            que4 = input("Vill du fortsätta: ")

            if que4 == "j":
                name5 = input("Skriv ett namn här: ").lower()

else:
    quit()

list = [name1, name2, name3, name4, name5]
print(list)