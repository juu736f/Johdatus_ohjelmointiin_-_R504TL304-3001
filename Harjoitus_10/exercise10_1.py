import os
os.chdir(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))))
with open("artists.txt","rt") as file:
    data = [line.rstrip() for line in file]
    
for i in range(len(data)):
    print(data[i])