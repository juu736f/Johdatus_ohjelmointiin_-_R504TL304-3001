def main():
    keskikulutus = float(6.5)
    try:
        matkaInKm = float(input("Anna matka kilometreinä: "))
    except ValueError:
        print("Virheellinen syöte. Anna numero.")
        return 0
    if matkaInKm < 0:
        print("Matka ei voi olla negatiivinen")
        return 0
    kokonaiskulutus = (keskikulutus * matkaInKm) / 100
    print(f"Polttoaineen kulutus on {kokonaiskulutus:.1f} litraa")

if __name__ == "__main__":
    main()