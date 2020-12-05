#5

import datetime
import shutil

flytta = input("Skriv länk till den fil du vill flytta? ").lower()
adress = input("Skriv länk till den fil du vill flytta? ").lower()

shutil.move(flytta, adress)

file = open('c:\\ITS20\\test\\skaflyttas.txt')
file.write(f"{datetime.datetime.now()}\n")
