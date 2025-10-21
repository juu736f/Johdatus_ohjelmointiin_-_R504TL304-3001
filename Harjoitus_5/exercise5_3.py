import sys
pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128
def main():
    try:
        radius = float(input("Anna säde:\n> "))
    except ValueError:
        print("Anna luku.")
        main()
    print(f"Pinta-ala: {pow(pi*radius,2)}")
    while True:
        try:
            retry = str(input("Haluatko jatkaa? (k/e)\n> "))
        except ValueError:
            print("Valitse kyllä tai ei (k/e)")
        if retry.lower() == "k":
            main()
        if retry.lower() == "e":
            sys.exit()
        else: 
            print("Valitse kyllä tai ei (k/e)")
            
if __name__ == "__main__":
    main()