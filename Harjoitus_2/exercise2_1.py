pi = 3.141592653589793238462643383279

def init():
    print("Valitse vaihtoehto:\n1) Laske särmiön tilavuus\n2) Laske pallon tilavuus")
    try:
        userChoice = int(input("Anna valintasi: "))
    except ValueError: 
        print("Virheellinen syöte. Yritä uudelleen.")
        init()
    if userChoice == 1 or userChoice == 2:
        return userChoice
    else:
        print("Virheellinen valinta. Yritä uudelleen.")
        init()

# V = a * b * c
def sarmioKysymykset():
    a = input("Anna särmiön korkeus: ")
    b = input("Anna särmiön leveys: ")
    c = input("Anna särmiön syvyys: ")
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print("Yksi tai useampi virheellinen syöte. Yritä uudelleen.")
        return
    tilavuus = a * b * c
    print(f"Särmiön tilavuus on: {tilavuus:.2f} m³")
    return tilavuus

# V = 4/3 * π * r^3
def palloKysymykset():
    try:
        r = float(input("Anna pallon säde: "))
    except ValueError:
        print("Virheellinen syöte. Yritä uudelleen.")
        return
    tilavuus = (4/3) * pi * (r ** 3)
    print(f"Pallon tilavuus on: {tilavuus:.2f} m³")

def main():
    choice = init()
    if choice == 1:
        sarmioKysymykset()
    elif choice == 2:
        palloKysymykset()
    else:
        print("Väärä valinta. Yritä uudelleen.")
        main()

if __name__ == "__main__": 
    main()
