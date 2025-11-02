import re
orderList = ("T1565_2020", "T2432_2019", "T8551_2018", "T3442_2019", "T9814_2018", "T7733_2020")

def main():
    try:
        year = None
        year = int(input("Anna vuosiluku:\n> "))
    except ValueError:
        print("Anna kokonaisluku.")
        main()
    pattern = "[A-Za-z0-9]+_" + str(year)
    for order in orderList:
        if re.match(pattern, order):
            print(f"{order.split("_", 1)[0]}")
        
if __name__ == "__main__":
    main()

    