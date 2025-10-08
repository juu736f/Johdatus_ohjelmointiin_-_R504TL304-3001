import sys

def main():
    try:
        word = input("Syötä sana: \n")
    except ValueError:
        print("Väärä syöte")
        sys.exit()
    if word:
        reversedWord = makeAndReverseWord(word)
        if (checkPalindrome(reversedWord, word) == True):
            print(reversedWord)
            print(f"Merkkisarja {word} on palindromi")
        else:
            print(reversedWord)
            print(f"Merkkisarja {word} ei ole palindromi")
            sys.exit
    else:
        print("Antamasi teksti on tyhjä.”")
        sys.exit()
    
    
def checkPalindrome(reversedWord, word):
    if reversedWord == word:
        return True
    else:
        return False
        
def makeAndReverseWord(word):
    wordList = list(word)
    wordList.reverse()
    reversedWord = ''.join(wordList)
    return reversedWord
    
if __name__ == "__main__":
    main()
        
        

