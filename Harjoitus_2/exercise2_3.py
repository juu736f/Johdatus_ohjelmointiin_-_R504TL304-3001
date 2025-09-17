def verolaskuri():
    try:
        kkPalkka = float(input("Anna kuukausipalkka: "))
        if kkPalkka < 0:
            print("Kuukausipalkan tulee olla positiivinen luku.")
            return
    except ValueError:
        print("Virheellinen syöte. Anna numeerinen arvo.")
        return
    try:
        veroProsentti = float(input("Anna veroprosentti: "))
        if veroProsentti < 0 or veroProsentti > 100:
            print("Veroprosentin tulee olla välillä 0-100.")
            return
    except ValueError:
        print("Virheellinen syöte. Anna numeerinen arvo.")
        return
    veroOsuus = kkPalkka * (veroProsentti / 100)
    print(f"Kuukausipalkka: {kkPalkka:.2f} €")
    print(f"Veron osuus ({veroProsentti:.0f}%): {veroOsuus:.2f} €")
    print(f"Nettopalkka: {kkPalkka - veroOsuus:.2f} €")

if __name__ == "__main__":
    verolaskuri()