# coding: iso-8859-1 -*-

try:
    luku = int(input("Anna kokonaisluku: \n"))
except ValueError:
    print("Väärä syöte")
    exit()


    
if luku % 3 == 0 or luku % 5 == 0:
    jako = True
else:
    jako = False
    
if jako == True:
    print(f"Luku {luku} on jaollinen kolmella tai viidellä")
else:
    print(f"Luku {luku} ei ole jaollinen kolmella tai viidellä")
