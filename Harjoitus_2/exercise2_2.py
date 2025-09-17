import math

def hypotenuusa(a, b):
    hypotenuusa = math.sqrt(a**2 + b**2)
    return hypotenuusa

def main():
    try:
        a = float(input("Anna kateetti: "))
        b = float(input("Anna toinen kateetti: "))
    except ValueError:
        print("Virheellinen syöte. Yritä uudelleen.")
        return
    hypotenuusa(a, b)
    print(f"Hypotenuusa on: {hypotenuusa(a, b):.2f}")

if __name__ == "__main__":
    main()