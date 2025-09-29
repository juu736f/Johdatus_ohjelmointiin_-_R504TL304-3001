import sys

def karkausvuosiChecker(vuosi):
    if (vuosi % 4 == 0) and (vuosi % 100 != 0) or (vuosi % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        vuosi = int(input("Anna vuosi: "))
    except ValueError:
        print("Anna numero.")
        sys.exit()
    if karkausvuosiChecker(vuosi) == True:
        print(f"{vuosi} on karkausvuosi.")
    else:
        print(f"{vuosi} ei ole karkausvuosi.")
    
if __name__ == "__main__":
    main()