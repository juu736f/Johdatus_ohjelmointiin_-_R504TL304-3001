import sys
gradeList = []
def main():
    try:
        studentAmount = int(input(f"Anna oppilaiden lukumäärä:\n> "))
    except ValueError:
        print("Anna kokonaisluku")
        sys.exit()
    for i in range(studentAmount):
        try:
            grade = int(input(f"Anna oppilaan {i+1} arvosana:\n> "))
        except ValueError:
            print("Anna kokonaisluku")
            sys.exit()
        if 1 <= grade <= 5:
            gradeList.append(grade)
        else:
           print("Luvun täytyy olla 1-5 väliltä.")
           sys.exit()
    classAverage = sum(gradeList) / studentAmount
    if 0 <= classAverage < 1:
        classStatus = "Huono tulos"
    elif 1 <= classAverage < 2:
        classStatus = "Heikko tulos"
    elif 2 <= classAverage < 3:
        classStatus = "Tyydyttävä tulos"
    elif 3 <= classAverage < 4:
        classStatus = "Hyvä tulos"
    elif 4 <= classAverage <= 5:
        classStatus = "Kiitettävä tulos"
    else:
        print("Tuntematon virhe. Tämän ei pitäisi tapahtua.")
        sys.exit()
    
    print(f"Luokan keskiarvo: {classAverage}")
    print(f"Luokan status: {classStatus}")
    
if __name__ == "__main__":
    main()