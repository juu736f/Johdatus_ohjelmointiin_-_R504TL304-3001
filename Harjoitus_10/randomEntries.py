import uuid
import datetime
import secrets
import os
import json
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))
fileName = "guestbook.json"

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

while True:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password1 = ''.join(secrets.choice(alphabet) for i in range(8))
    password2 = ''.join(secrets.choice(alphabet) for i in range(12))
    writeToGuestbook(password1, password2)