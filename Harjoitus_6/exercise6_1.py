import sys
numberList = []
sijaluku = ("ensimmäinen", "toinen", "kolmas", "neljäs", "viides")
for i in range(5):
    try:
        number = int(input(f"Anna {sijaluku[i]} numero.\n> "))
    except ValueError:
        print(f"Väärä syöte.")
        sys.exit()
    if number < 0:
        print(f"Anna positiivinen luku")
        sys.exit()
    else:
        numberList.append(number)
numberList.sort(reverse=True)
print(f"Suurin annettu numero: {numberList[0]}")