import sys

def main():
    try:
        tunnit = float(input("Anna työtuntien määrä: "))
    except ValueError:
        print("Anna numero.")
        sys.exit()
    try:
        palkka = float(input("Anna tuntipalkka: "))
    except ValueError:
        print("Anna numero.")
        sys.exit()
    if tunnit >= 40:
        ylityot = tunnit - 40
        palkka = (40 * palkka) + (ylityot * (palkka * 1.5))
        print(f"Palkka on {palkka} euroa.")
    else:
        palkka = tunnit * palkka
        print(f"Palkka on {palkka} euroa.")
        
if __name__ == "__main__":
    main()
    