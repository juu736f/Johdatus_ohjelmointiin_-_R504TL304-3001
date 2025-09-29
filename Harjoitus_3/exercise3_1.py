import sys

def main():
    try:
        numero1 = float(input("Anna ensimmäinen numero: "))
    except ValueError:
        print("Anna numero.")
        sys.exit()
    try:
        numero2 = float(input("Anna toinen numero: "))
    except ValueError:
        print("Anna numero.")
        sys.exit()
    if numero1 > numero2:
        print(f"{numero1} on suurempi kuin {numero2}")
        sys.exit()
    elif numero1 == numero2:
        print(f"{numero1} on yhtä suuri kuin {numero2}")
        sys.exit()
    else:
        print(f"{numero1} on pienempi kuin {numero2}")
        sys.exit()
        
if __name__ == "__main__":
    main()