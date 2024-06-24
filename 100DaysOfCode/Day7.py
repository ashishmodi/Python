import random
import resources.Day7_HangmanGame.hangman_art as art
import resources.Day7_HangmanGame.hangman_words as words
#from replit import clear     # clear() function

# print(art.logo)     # another way below
from resources.Day7_HangmanGame.hangman_art import logo, stages
print(logo)
# lsWords = ["tiger", "lion", "hippopotamus"]   # TESTING use it from file
sChosenWord = random.choice(words.word_list)
print(f"Random word for Hangman game is {sChosenWord}")

lsChosenWord = []
# for i in range(0, len(sChosenWord)):    # lion 0 1 2 3 => 4 char
    # lsChosenWord.append("_")
# optimized way
for _ in range(len(sChosenWord)):
    lsChosenWord += "_"

nDrawCounter = len(stages) - 1
bEndOfGame = False
bWon = False

while not bEndOfGame:
    sUserLetter = input("Enter a letter: ").lower()

    if not sChosenWord.count(sUserLetter) > 0:
        print(stages[nDrawCounter])
        nDrawCounter -= 1
        if nDrawCounter < 0:            
            bEndOfGame = True
        continue

    i = 0
    for ch in sChosenWord:
        if ch == sUserLetter:
            lsChosenWord[i] = ch
        i += 1

    if lsChosenWord.count("_") == 0:
        bEndOfGame = True
        bWon = True

if bWon:
    print(f"Game over! You have won! {lsChosenWord}")
else:
    print("Game over! You have lost.")