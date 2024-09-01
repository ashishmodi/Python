############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random

def printResult(lsPlayersRandomCards, lsCpusRandomCards):
    print(f"Player's final cards: {lsPlayersRandomCards}, Cpu's final cards: {lsCpusRandomCards}")
    print(f"Player's score: {sum(lsPlayersRandomCards)}, CPU's score: {sum(lsCpusRandomCards)}")
    sResult = "Player won!" if sum(lsPlayersRandomCards) > sum(lsCpusRandomCards) else "CPU Won!"
    if sum(lsPlayersRandomCards) == sum(lsCpusRandomCards):
        sResult = "Game Draw!"
    elif sum(lsPlayersRandomCards) > 21 and sum(lsCpusRandomCards) > 21:
        sResult = "Both overshoot!"
    elif sum(lsPlayersRandomCards) > 21:        
        sResult = "CPU won!"
    elif sum(lsCpusRandomCards) > 21:
        sResult = "Player won!"
    print(sResult)
    
def deal_card():
    lsCards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # nPlayersFirstNo = random.randint(lsCards[0], lsCards[len(lsCards) - 1])
    # nPlayersFirstNo = random.randint(1, 10)
    # lsPlayersRandomCards = random.sample(lsCards, 2)      # selects 2 cards
    return random.choice(lsCards)

sPickAnotherCard = input("Do you want to play the Blackjack game? ")
bContinuePlay = True if sPickAnotherCard == "yes" else False
while bContinuePlay:
    lsPlayersRandomCards = []
    lsCpusRandomCards = []
    print("\n" * 20)
    for _ in range(2):
        lsPlayersRandomCards.append(deal_card())
        lsCpusRandomCards.append(deal_card())
    
    print(f"Player's cards: {lsPlayersRandomCards}, Cpu's first card: {lsCpusRandomCards[0]}")
    
    while sum(lsCpusRandomCards) != 21 and sum(lsCpusRandomCards) < 17:
        lsCpusRandomCards.append(deal_card())
    
    while sum(lsPlayersRandomCards) < 21:
        sPickAnotherCard = input("Do you want to pick another card? ")
        if sPickAnotherCard == "yes":
            lsPlayersRandomCards.append(deal_card())
            if sum(lsPlayersRandomCards) > 21:
                if lsPlayersRandomCards.count(11) > 0:
                    print("Replacing Ace card value with 1 instead of 11 as score is exceeding 21")
                    # lsPlayersRandomCards = list(map(lambda x: x.replace(11, 1), lsPlayersRandomCards))    # only works for string
                    # lsPlayersRandomCards = [1 if i == 11 else i for i in lsPlayersRandomCards]    # replace
                    lsPlayersRandomCards.remove(11)
                    lsPlayersRandomCards.append(1)
                if sum(lsPlayersRandomCards) > 21:
                    printResult(lsPlayersRandomCards, lsCpusRandomCards)
                    break
            print(f"Player's cards: {lsPlayersRandomCards}")
        elif sPickAnotherCard == "no":
            printResult(lsPlayersRandomCards, lsCpusRandomCards)            
            break
        
    if sum(lsPlayersRandomCards) >= 21:
        printResult(lsPlayersRandomCards, lsCpusRandomCards)
    
    sPickAnotherCard = input("Do you want to play the Blackjack game again? ")
    bContinuePlay = True if sPickAnotherCard == "yes" else False
    


# Do you want to play the Blackjack game again? yes
# Player's cards: [11, 2], Cpu's first card: 10
# Do you want to pick another card? yes
# Replacing Ace card value with 1 instead of 11 as score is exceeding 21
# Player's cards: [1, 2, 1]
# Do you want to pick another card? yes
# Player's cards: [1, 2, 1, 7]
# Do you want to pick another card? yes
# Player's cards: [1, 2, 1, 7, 8]
# Do you want to pick another card? no
# Player's final cards: [1, 2, 1, 7, 8], Cpu's final cards: [10, 10]
# Player's score: 19, CPU's score: 20
# CPU Won!