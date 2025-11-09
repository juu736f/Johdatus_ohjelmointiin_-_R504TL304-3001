fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]
inventory = [fruits, berries, vegetables]

for i in inventory:
    for item in i:
        print(item)