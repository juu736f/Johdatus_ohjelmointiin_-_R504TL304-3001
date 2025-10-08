from datetime import datetime

nyt = datetime.now()
paivamaara = nyt.strftime("%d.%m.%Y")
asiakkaanNimi = "Matti Meikäläinen"
syntymavuosi = "1984"
saldo = 345

print(f"{asiakkaanNimi} ({syntymavuosi}), saldo: {saldo:.2f} €, päivitetty {paivamaara}")