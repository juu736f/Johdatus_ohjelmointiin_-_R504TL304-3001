import sys

def main():
    try:
        lampotila = float(input("Anna lämpötila: "))
    except ValueError:
        print("Anna numero.")
        sys.exit()
    if 0 <= lampotila <= 10:
        print("KYLMÄÄ")
    elif 11 <= lampotila <= 15:
        print("KOLEAA")
    elif 16 <= lampotila <= 20:
        print("MELKO LÄMMINTÄ")
    elif 21 <= lampotila <= 25:
        print("LÄMMINTÄ")
    elif 26 <= lampotila <= 30:
        print("HELLETTÄ")
    else:
        print("Lämpötila ei ole annetulla välillä.")
        sys.exit()
        
if __name__ == "__main__":
    main()