import os
guestBook = "guestbook.txt"
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))
while True:
    try:
        status = input("Haluatko lukea vai kirjoittaa vieraskirjaan? ([r]ead/[W]rite)\n> ").lower()
    except ValueError:
        print("Yritä uudelleen.")
    break
if status == "r" or status =="read":
    try:
        with open(guestBook,"r") as file:
            print(file.readline())
    except FileNotFoundError:
        print("Tiedostoa ei löydy")
else:
    with open(guestBook,"a") as file:
        file.write(str(input("Anna nimesi:\n> "))+"\n")
