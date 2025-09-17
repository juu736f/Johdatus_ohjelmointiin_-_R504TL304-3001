# ax^2 + bx + c = 0
# a, b, c ∈ R
# a != 0
# Kysy käyttäjältä eri muuttujien arvot (a, b ja c),
# ja tulosta lopuksi
# vastaus (eli x:n arvo(t)).

import cmath
import sys

def kysely():
    try:
        a = float(input("Syötä arvo muuttujalle a: "))
        b = float(input("Syötä arvo muuttujalle b: "))
        c = float(input("Syötä arvo muuttujalle c: "))
    except ValueError:
        print("Virheellinen syöte. Käytä numeerista arvoa.")
        sys.exit()
    
    if a == 0:
        print("a ei voi olla 0")
        sys.exit()
    else:
        return a, b, c

def ratkaisija(a, b, c):
    dis = (b**2) - (4 * a * c)
    ans1 = (-b - cmath.sqrt(dis)) / (2 * a)
    ans2 = (-b + cmath.sqrt(dis)) / (2 * a)
    return ans1, ans2

def main():
    a, b, c = kysely()
    ans1, ans2 = ratkaisija(a, b, c)
    
    # Check if solutions are real or complex
    if ans1.imag == 0 and ans2.imag == 0:
        # Real solutions
        print(f"Ratkaisut ovat: {ans1.real} ja {ans2.real}")
    else:
        # Complex solutions
        print(f"Ratkaisut ovat: {ans1} ja {ans2}")

if __name__ == "__main__":
    main()