def main():
    verotonHinta, alv = alvValinnat()
    verotonHinta = float(verotonHinta)
    alvOsa, verollinenHinta, alv = alvLaske(verotonHinta, alv)
    alvTulosta(verotonHinta, alvOsa, verollinenHinta, alv)

def alvValinnat():
    verotonHinta = input("Anna veroton hinta: ")
    print("1) 0%\n2) 10%\n3) 14%\n4) 25,5%")
    alvInput = input("Valitse alv-prosentti: ")
    if alvInput == "1":
        alv = 0
    elif alvInput == "2":
        alv = 0.10
    elif alvInput == "3":
        alv = 0.14
    elif alvInput == "4":
        alv = 0.255
    else:
        print("Virheellinen valinta, yritä uudelleen.")
        alvValinnat()
    return verotonHinta, alv

def alvLaske(verotonHinta, alv):
    alvOsa = verotonHinta * alv
    verollinenHinta = verotonHinta + alvOsa
    return alvOsa, verollinenHinta,alv

def alvTulosta(verotonHinta, alvOsa, verollinenHinta, alv):
    print(f"Veroton hinta: {verotonHinta:.2f} €")
    print(f"ALV ({alv * 100}%): {alvOsa:.2f} €")
    print(f"Verollinen hinta: {verollinenHinta:.2f} €")

if __name__ == "__main__":
    main()