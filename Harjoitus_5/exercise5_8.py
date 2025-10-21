encryptedList = []
cleartext = str(input("Anna lause, jonka haluat salata:\n> "))
cipher = int(input("Anna siirtoluku:\n> "))
clearlist=list(cleartext)

for i in clearlist:
    orderNumber = ord(i)
    if orderNumber == 32:
        encryptedList.append(" ")
        continue
    orderNumber += cipher
    encryptedList.append(chr(orderNumber))

encrypted = "".join(encryptedList)
print(encrypted)