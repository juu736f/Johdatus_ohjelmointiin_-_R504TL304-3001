movies = [
    {"name": "Komisario Palmun erehdys", "year": 1960},
    {"name": "Kauas pilvet karkaavat", "year": 1996},
    {"name": "Komisario Palmun erehdys", "year": 2002},
    {"name": "Игла (Igla)", "year": 1988},
    {"name": "The Godfather", "year": 1972},
    {"name": "Tuntematon sotilas", "year": 1955},
    {"name": "Сталкер (Stalker)", "year": 1979},
    {"name": "Pulp Fiction", "year": 1994},
    {"name": "Mies vailla menneisyyttä", "year": 2002},
    {"name": "Брат (Brother)", "year": 1997},
    {"name": "Back to the Future", "year": 1985},
    {"name": "Talvisota", "year": 1989},
    {"name": "Летят журавли (The Cranes Are Flying)", "year": 1957},
    {"name": "The Shawshank Redemption", "year": 1994},
    {"name": "Hytti nro 6", "year": 2021},
    {"name": "Ирония судьбы (Irony of Fate)", "year": 1976},
    {"name": "Forrest Gump", "year": 1994},
    {"name": "Rare Exports: A Christmas Tale", "year": 2010},
    {"name": "Солярис (Solaris)", "year": 1972},
    {"name": "The Matrix", "year": 1999},
    {"name": "Valkoinen peura", "year": 1952},
    {"name": "Левиафан (Leviathan)", "year": 2014},
    {"name": "Star Wars: A New Hope", "year": 1977},
    {"name": "Sisu", "year": 2022},
    {"name": "Иди и смотри (Come and See)", "year": 1985},
    {"name": "Blade Runner", "year": 1982},
    {"name": "Poika ja ilves", "year": 1998},
    {"name": "Москва слезам не верит (Moscow Does Not Believe in Tears)", "year": 1980},
    {"name": "The Dark Knight", "year": 2008},
    {"name": "Kaasua, komisario Palmu!", "year": 1961},
    {"name": "Броненосец «Потёмкин» (Battleship Potemkin)", "year": 1925},
    {"name": "E.T. the Extra-Terrestrial", "year": 1982},
    {"name": "Puhdistus", "year": 2012},
    {"name": "Андрей Рублёв (Andrei Rublev)", "year": 1966},
    {"name": "Goodfellas", "year": 1990},
    {"name": "Le Havre", "year": 2011},
    {"name": "Бриллиантовая рука (The Diamond Arm)", "year": 1969},
    {"name": "Inception", "year": 2010},
    {"name": "Toivon tuolla puolen", "year": 2017},
    {"name": "Кин-дза-дза! (Kin-dza-dza!)", "year": 1986},
    {"name": "Fight Club", "year": 1999},
    {"name": "Kahdeksan surmanluotia", "year": 1972},
    {"name": "Человек с киноаппаратом (Man with a Movie Camera)", "year": 1929},
    {"name": "Saving Private Ryan", "year": 1998},
    {"name": "Helmiä ja sikoja", "year": 2003},
    {"name": "Нелюбовь (Loveless)", "year": 2017},
    {"name": "Alien", "year": 1979},
    {"name": "Juha", "year": 1999},
    {"name": "Война и мир (War and Peace)", "year": 1966},
    {"name": "Oppenheimer", "year": 2023},
    {"name": "Pahat pojat", "year": 2003}
]
moviesBefore2000 = []
moviesAfter2000 = []
for i in range(len(movies)):
    if 2000 > movies[i]["year"]:
        moviesBefore2000.append(movies[i]["name"])
for i in range(len(movies)):
    if 2000 <= movies[i]["year"]:
        moviesAfter2000.append(movies[i]["name"])
        
print(f"Ennen 2000-lukua julkaistut elokuvat: {', '.join(map(str,moviesBefore2000))}")
print(f"\nJälkeen 2000-luvun julkaistut elokuvat: {', '.join(map(str,moviesAfter2000))}")    
