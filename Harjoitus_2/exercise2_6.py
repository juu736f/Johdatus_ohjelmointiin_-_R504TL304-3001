# ax^2 + bx + c = 0
# a, b, c ∈ R
# a != 0
# Kysy käyttäjältä eri muuttujien arvot (a, b ja c),
# ja tulosta lopuksi vastaus (eli x:n arvo(t)).

import math
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
    discriminant = (b**2) - (4 * a * c)
    
    if discriminant > 0:
        # Two real solutions
        ans1 = (-b - math.sqrt(discriminant)) / (2 * a)
        ans2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return ans1, ans2, "real"
    elif discriminant == 0:
        # One real solution
        ans = -b / (2 * a)
        return ans, ans, "real"
    else:
        # Complex solutions
        real_part = -b / (2 * a)
        imag_part = math.sqrt(abs(discriminant)) / (2 * a)
        return (real_part, -imag_part), (real_part, imag_part), "complex"

def main():
    a, b, c = kysely()
    ans1, ans2, solution_type = ratkaisija(a, b, c)
   
    if solution_type == "real":
        if ans1 == ans2:
            print(f"Ratkaisu on: {ans1}")
        else:
            print(f"Ratkaisut ovat: {ans1} ja {ans2}")
    else:
        # Complex solutions
        if ans1[1] < 0:
            print(f"Ratkaisut ovat: {ans1[0]}{ans1[1]}i ja {ans2[0]}+{ans2[1]}i")
        else:
            print(f"Ratkaisut ovat: {ans1[0]}+{ans1[1]}i ja {ans2[0]}+{ans2[1]}i")

if __name__ == "__main__":
    main()