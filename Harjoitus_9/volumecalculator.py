import functions as f
import sys
def main():
    while True:
        try:
            userChoice = str(input("Valitse:\n1. Särmiön tilavuus\n2. Pallon tilavuus\n3. Putken tilavuus\n0. sys.exit()\n> "))
        except ValueError:
            print("Väärä syöte")
        if userChoice == "1":
            print(f.box_volume(int(input("Anna pituus x\n> ")),int(input("Anna pituus y\n> ")),int(input("Anna pituus z\n> "))))
            break
        elif userChoice == "2":
            print(f.ball_volume(int(input("Anna säde"))))
            break
        elif userChoice == "3":
            print(f.pipe_volume(int(input("Anna säde")),int(input("Anna pituus"))))
            break
        elif userChoice == "0":
            sys.exit()
        else:
            print("Väärä syöte\n")    
    while True:
        retry = str(input("Haluatko yrittää uudelleen? (y/n)\n> "))
        if retry.lower() in ["n", "no"]:
            sys.exit()
        elif retry.lower() in ["y", "yes"]:
            main()
            break
        else:
            print("Väärä syöte\n")
            
if __name__ == "__main__":
    main()