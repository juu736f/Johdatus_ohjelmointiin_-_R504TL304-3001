import json
import datetime
import uuid
import os
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))
fileName = "guestbook.json" 

if os.path.exists(fileName) == False:
        open(fileName, 'a').close()

def writeToGuestbook(name, message):
    data = {
    str(uuid.uuid4()): {
        "name": name,
        "message": message,
        "formattedTime": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "epochTime": datetime.datetime.now(datetime.timezone.utc).timestamp()
    }
}
    if os.path.exists(fileName):
        try:
            with open(fileName, "r") as file:
                fileData = json.load(file)
        except json.JSONDecodeError:
            fileData = {}
    else:
        fileData = {}
        
    fileData.update(data)

    with open(fileName, "w") as file:
        json.dump(fileData,file,indent=4)
    return uuid

#0 = uuid
#1 = name
#2 = message
def readFromGuestbook(type, name, message, uuid):
    with open(fileName, 'r') as file:
        data = json.load(file)
    results = []
    match type:
        case 0:  # hae uuid perusteella
            entry = data.get(uuid)
            if entry:
                results.append((uuid, entry["name"], entry["message"], entry["formattedTime"], entry["epochTime"]))
        case 1:  # hae "name" perusteella
            for key, entry in data.items():
                if entry["name"] == name:
                    results.append((key, entry["name"], entry["message"], entry["formattedTime"], entry["epochTime"]))
        case 2:  # hae "message" perusteella
            for key, entry in data.items():
                if entry["message"] == message:
                    results.append((key, entry["name"], entry["message"], entry["formattedTime"], entry["epochTime"]))
    return results if results else None

def getParent(data, type, target):
    for uuid in data:
            if (data[uuid][type]) == target:
                return uuid
        
def main():
    while True:
        try:
            action = str(input("Haluatko kirjoittaa vai hakea vieraskirjasta? ([S]earch, [w]rite\n> ")).lower()
        except ValueError:
            print("Väärä syöte")
        if action == "s" or action == "search":
            try:
                action = int(input("Haluatko hakea UUID:n, nimimerkin vai viestin pohjalta?\n1) UUID\n2) Nimimerkki\n3) Viesti\n> "))
            except ValueError:
                print("Väärä syöte")
            match action:
                case 1:
                    uuid = str(input("Anna UUID:\n> "))
                    try:
                        data = readFromGuestbook(action-1, None, None, uuid)
                    except TypeError:
                        print("Ei hakutuloksia.")
                        main()
                    printSearchResults(data)
                    main()
                case 2:
                    name = str(input("Anna nimi:\n> "))
                    try:
                        data = readFromGuestbook(action-1, name, None, None)
                    except TypeError:
                        print("Ei hakutuloksia.")
                        main()
                    printSearchResults(data) 
                case 3:
                    message = str(input("Anna viesti:\n> "))
                    try:
                        data = readFromGuestbook(action-1, None, message, None)
                    except TypeError:
                        print("Ei hakutuloksia.")
                        main()
                    printSearchResults(data)
                case _:
                    print("Väärä syöte.")
        else:
            try:
                writeToGuestbook(str(input("Anna nimimerkki:\n> ")),str(input("Anna viesti:\n> ")))
                main()
            except Exception as e:
                print(f"Tapahtui virhe.\n{e}")
            print("Vieraskirjaan kirjoitettu onnistuneesti!")
            main()

def printSearchResults(data):
    print("Hakutulokset:\n---------------")
    if not data:
        print("Ei hakutuloksia.")
        return
    for i, result in enumerate(data):
        try:
            uuid, name, message, formattedTime, epochTime = result
        except (TypeError, IndexError):
            print("Virhe hakutulosten käsittelyssä.")
            continue
        print(f"Hakutulos {i+1}:\n\nUUID: {uuid}\nNimi: {name}\nViesti: {message}\nAika: {formattedTime}\nUnix-aika: {epochTime}\n---------------")
        
if __name__ == "__main__":
    main()