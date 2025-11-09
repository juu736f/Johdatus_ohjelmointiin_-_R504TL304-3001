shopcart = [ 
    {
        "name": "Lokki-valaisin", 
        "price": 349.9
    }, 
    {
        "name": "Stockholm-matto",
        "price": 129.9
    }, 
    {
        "name": "Malm-lipasto",
        "price": 49.9
    }, 
    {
        "name": "Vienna-divaanisohva",
        "price": 799.9
    }, 
    {
        "name": "Ritz-nojatuoli",
        "price": 369.9
    } 
]
total = 0
print("Kuitti ostoksistasi:")
for i in range(len(shopcart)):
    print(f"- {shopcart[i]["name"]}")
for i in range(len(shopcart)):
    total += shopcart[i]["price"]
print(f"\nYhteensä: {total:.2f} €\nTervetuloa uudelleen!")