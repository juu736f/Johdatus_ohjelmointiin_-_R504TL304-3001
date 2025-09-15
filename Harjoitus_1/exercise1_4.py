def minuutitTunneiksi(minuutit):
    tunnit = minuutit // 60
    minuutit = minuutit % 60
    return (tunnit, minuutit)

def main():
    try:
        minuutit = int(input("Anna minuuttien määrä: "))
    except ValueError:
        print("Virheellinen syöte. Anna kokonaisluku.")
        return
    if minuutit < 0:
        print("Minuuttien määrä ei voi olla negatiivinen.")
        return
    tunnit, minuutit = minuutitTunneiksi(minuutit)
    if tunnit == 0:
        print(f"{minuutit} minuuttia")
    elif minuutit == 0:
        print(f"{tunnit} tuntia")
    else:
        print(f"{tunnit} tuntia ja {minuutit} minuuttia")

if __name__ == "__main__":
    main()