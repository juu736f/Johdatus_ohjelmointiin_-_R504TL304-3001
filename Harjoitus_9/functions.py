import re
import os
import platform
pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019

def show_personal_info():
    print(f"Juuso Kekonen\nRanua\nOperations Staff")
    
def count_seconds(h,m,s):
    m += h * 60 
    s += m * 60
    return s

def magazine_serial_check(serial):
    if re.search(r"^\d{4}-\d{4}", serial) == None:
        return False
    else:
        return True
    
def show_numbered_list(title, data):
    print(title, "\n")
    for number, name in enumerate(data):
        print(f"{number+1}. {name}")
    
def parse_participants_data(data):
    people = data.split(",")
    people = [p.strip() for p in people]
    return people

def alphabetise_participants_data(data):
    byLastName = sorted([" ".join(reversed(d.split(" "))) for d in data])
    byFirstName = sorted([" ".join(d.split(" ")) for d in data])
    byOriginal = data
    return byLastName, byFirstName, byOriginal

def box_volume(x,y,z):
    return round((x*y*z),2)

def ball_volume(r):
    return round(((4*pi) * (r**3) / 3),2)

def pipe_volume(r,x):
    return round((pi * (r**2) * x),2)

def recurseDirectoriesFromRoot():
    if platform.system() == "Windows" or "ReactOS":
        root = "C:\\"
    if platform.system() == "Linux" or "Darwin" or "SunOS":
        root = "/"
    else:
        print("Järjestelmäsi ei ole yhteensopiva. Oikeasti en vaan jaksa/halua selvittää miten järjestelmäsi tiedostojärjestelmä pelaa.")
    for root, dirs, files in os.walk(root):
        path = root.split(os.sep)
        print((len(path) - 1) * '.', os.path.basename(root))
        for file in files:
            print(len(path) * '.', file)

