basket = ["omena","banaani","kirsikka","porkkana","peruna","tomaatti","kaali"]

def main():
    product = str(input("Anna sana:\n> "))
    
    for i in range(len(basket)):
        if basket[i] == product:
            print("Sana löytyi!")
            break
        print("Etsitään...")
    
    
    deleteProduct = str(input("Anna poistettava sana:\n> "))
    if deleteProduct.isnumeric() == True:
        basket.pop(int(deleteProduct) - 1)
    else:
        basket.remove(deleteProduct)
        
    for i in range(len(basket)):
        print(basket[i])
if __name__ == "__main__":
    main()