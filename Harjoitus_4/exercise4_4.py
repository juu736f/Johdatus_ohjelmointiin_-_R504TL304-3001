# coding: iso-8859-1 -*-
import sys

try:
    nro1 = float(input("Ensimmäinen numero: \n"))
except ValueError:
    print("Väärä syöte")
    sys.exit()
try:
    nro2 = float(input("Toinen numero: \n"))
except ValueError:
    print("Väärä syöte")
    sys.exit()

if nro1 == 0 or nro2 == 0:
    print("Nollalla ei voi jakaa")
    sys.exit()

print(f"{nro1} / {nro2} = {nro1/nro2:.2f}")
