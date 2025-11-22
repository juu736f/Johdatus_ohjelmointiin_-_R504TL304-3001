import secrets
import os
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))
fileName = "wisewords.txt"
rows = sum(1 for _ in open(fileName))
randomInteger = int(secrets.choice(range(0,rows)))

with open(fileName, 'r') as file:
    lines = file.readlines()

print(f"Bonustilittäjän mietelauseita (osa {randomInteger+1}):")
print(lines[randomInteger])