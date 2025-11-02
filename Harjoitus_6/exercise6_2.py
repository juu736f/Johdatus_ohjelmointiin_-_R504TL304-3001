import sys

def main():
    try:
        multiplier = 0
        multiplier = float(input("Minkä luvun kertotaulun haluat nähdä? (1-10, 0 lopettaa ohjelman)"))
    except ValueError:
        print("Anna numero.")
        sys.exit
    if multiplier == 0:
        sys.exit()
    elif 1 <= multiplier <= 10:
        for i in range(10):
            x = i + 1
            print(f"{multiplier} x {i+1} = {multiplier*x}")
    main()
            
if __name__ == "__main__":
    main()