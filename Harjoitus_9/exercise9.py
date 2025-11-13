import functions as f
import sys

f.show_personal_info()
print(f.count_seconds(int(input("Anna tunnit:\n> ")), int(input("Anna minuutit:\n> ")), int(input("Anna sekunnit:\n> "))))
if f.magazine_serial_check(str(input("Anna sarjanumero\n> "))) == False:
    print("Sarjanumero ei ole oikea.")
else:  
    print("Sarjanumero on aito.")
names = str(input("Anna lista nimiä.\n> "))
byLastName, byFirstName, byOriginal = f.alphabetise_participants_data(f.parse_participants_data(names))
f.show_numbered_list("Nimet syöttöjärjestyksessä", byOriginal)
f.show_numbered_list("Nimet sukunimen mukaan", byLastName)
f.show_numbered_list("Nimet etunimen mukaan", byFirstName)
print(f.box_volume(int(input("Anna pituus x\n> ")),int(input("Anna pituus y\n> ")),int(input("Anna pituus z\n> "))))
print(f.ball_volume(int(input("Anna säde"))))
print(f.pipe_volume(int(input("Anna säde")),int(input("Anna pituus"))))

userChoice = input("Haluatko VARMASTI suorittaa recurseDirectoriesFromRoot() funktion? Tämä täyttää terminaali-ikkunasi. (y/n)\n> ").lower()

if userChoice == "n" or "no":
    sys.exit()
if userChoice == "y" or "yes":
    f.recurseDirectoriesFromRoot()
else:
    sys.exit()