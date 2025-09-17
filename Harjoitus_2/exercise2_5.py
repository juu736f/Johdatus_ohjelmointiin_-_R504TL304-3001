import secrets

def satunnaisLuku(min,max):
    return int(secrets.choice(range(min,max)))

def main():
    a = satunnaisLuku(1,10)
    print(f"Arvottu luku {a}")
    b = satunnaisLuku(1,10)
    print(f"Arvottu luku {b}")
    c = satunnaisLuku(1,10)
    print(f"Arvottu luku {c}")
    d = a*b*c
    print(f"Arvoituista luvuista laskettu pinta-ala: {d}")

if __name__ == "__main__":
    main()