mthList = ("Indeksi 0", "Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
while True:
    try:
        mthNumber = int(input("Anna kuukauden numero:\n> "))
        break
    except ValueError:
        print("Anna numero.")
        
if mthNumber == 0:
    print("Numero ei voi olla 0")
elif mthNumber > 12:
    print("Numero ei voi olla yli 12")
else:
    print(f"Kuukautesi on: {mthList[mthNumber]}")