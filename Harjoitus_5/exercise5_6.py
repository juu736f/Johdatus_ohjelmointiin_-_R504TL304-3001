movie = {
    "name":"Pulp Fiction",
    "year":1994,
    "director":"Quentin Tarantino",
    "genre":"Rikos, Draama",
    "duration":154
}

print("Silmukalla:\n")
for i in movie:
    print(movie[i])
print("----------\nIlman silmukkaa:\n")
print(movie["name"])
print(movie["year"])
print(movie["director"])
print(movie["genre"])
print(movie["duration"])
print("\n")