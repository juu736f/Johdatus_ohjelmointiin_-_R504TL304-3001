import sys
mthList = ("Indeksi 0", "Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")
mth = 0
rainAmountList = []
for i in range(12):
    mth += 1
    try:
        rainAmount = float(input(f"Anna {mthList[mth]}n sademäärä:\n> "))
    except ValueError as e:
        print(f"Virhe syötteessä. Anna numero.")
        sys.exit()
    rainAmountList.append(rainAmount)
print(f"Vuoden keskiarvo on n. {sum(rainAmountList)/12:.1f} mm")