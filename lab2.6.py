#6

setUsr = "abbe"
while setUsr != 1:

    usr = input("Ange ett användarnamn: ").lower()

    if usr == setUsr:
        print("Användarnamnet är korrekt")
        break

    else:
        print("Användarnamnet är felaktigt")


setPwd = "babbe"
while setPwd != 1:
    pwd = input("Ange ett lösenord: ").lower()

    if pwd == setPwd:
        print("Lösenordet är korrekt")
        break

    else:
        print("Lösenordet är felaktigt")
print("Du lyckades logga in!")
