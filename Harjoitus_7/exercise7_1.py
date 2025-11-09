cafe = { 
    "name": "Imaginary Cafe Oy", 
    "website": "https://edu.frostbit.fi/sites/cafe", 
    "categories": [ 
        "cafe", 
        "tea", 
        "lunch", 
        "breakfast" 
    ], 
    "location": { 
        "city": "Rovaniemi", 
        "address": "Testikuja 22", 
        "zip_code": "96200" 
    }    
} 
categories_list = cafe["categories"]
categories_string = ", ".join(categories_list)
print(f"{cafe["name"]}\n{cafe["location"]["address"]}\n{cafe["location"]["zip_code"]} {cafe["location"]["city"]}\n\n{cafe["website"]}\nPalvelut: {categories_string}")
