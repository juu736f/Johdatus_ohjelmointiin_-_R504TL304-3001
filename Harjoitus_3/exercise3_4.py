import sys

def main():
    try:
        pisteet = int(input("Anna pistemäärä: "))
    except ValueError:
        print("Anna numero.")
        sys.exit()
    if 0 <= pisteet <= 50:
        print("Arvosana on 0")
    elif 51 <= pisteet <= 60:
        print("Arvosana on 1")
    elif 61 <= pisteet <= 70:
        print("Arvosana on 2")
    elif 71 <= pisteet <= 80:
        print("Arvosana on 3")
    elif 81 <= pisteet <= 90:
        print("Arvosana on 4")
    elif 91 <= pisteet <= 100:
        print("Arvosana on 5")
    else:
        print("Pistemäärä ei ole annetulla välillä.")
        sys.exit()
        
if __name__ == "__main__":
    main()
    