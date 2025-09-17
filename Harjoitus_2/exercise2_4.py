def kulutusLaskuri(maantieajoKm, kaupunkiajoKm):
    maantieKulutusPer100 = 5.1
    kaupunkiKulutusPer100 = 7.5
    maantieKulutus = maantieajoKm * maantieKulutusPer100 / 100
    kaupunkiKulutus = kaupunkiajoKm * kaupunkiKulutusPer100 / 100
    return maantieKulutus + kaupunkiKulutus
    
def main():
    try:
        maantieajoKm = float(input("Anna maantieajon pituus (km): "))
        kaupunkiajoKm = float(input("Anna kaupunkiajon pituus (km): "))
    except ValueError:
        print("Virheellinen syöte. Anna numeerinen arvo.")
        return
    kokonaisKulutus = kulutusLaskuri(maantieajoKm, kaupunkiajoKm)
    print(f"Kokonaiskulutus: {kokonaisKulutus} litraa")

if __name__ == "__main__":
    main()