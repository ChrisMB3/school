#5
cat = input("Är du student, vuxen eller senior? ").lower()

if cat == "student" or "senior":
    print("Student/pensionärspris, din biljett kostar 20 kr.")

elif cat == "vuxen":
    print("Vuxenpris, din biljett kostar 30 kr")

else:
    print("Du har valt en felaktig kategori")