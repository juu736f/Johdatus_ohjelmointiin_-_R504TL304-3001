import sys

phrase = "The quick brown fox jumps over the lazy dog. That sentence contains every letter in the English alphabet. Isn’t that neat!"
phraseList = phrase.split()
for i, n in enumerate(phraseList):
    if n == "fox":
        phraseList[i] = "duck"
print(" ".join(phraseList))
try:
    deleteWord = str(input("Enter a word to delete: \n"))
except ValueError:
    print("Invalid input")
    sys.exit()
for i, n in enumerate(phraseList):
    if n == deleteWord:
        phraseList.remove(deleteWord)
print("\nLause, josta sana poistettu: \n" + " ".join(phraseList))
sys.exit()