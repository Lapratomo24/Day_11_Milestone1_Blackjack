## Blackjack ##

logo = '''
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  
'''

## Rules ##

# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0 # 0 represents blackjack
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

user_cards = []
computer_cards = []
game_end = False

for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
while not game_end:
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are {user_cards}, and your score is {user_score}.")
    print(f"Computer's first card is {computer_cards}.")

    if computer_score == 0 or user_score == 0 or user_score > 21:
        game_end = True
    else:
        draw_card = input("Would you like to draw another card? Type 'yes' or 'no': ")
        if draw_card == 'yes':
            user_cards.append(deal_card())
        elif draw_card == 'no':
            game_end = True
            print("Thank you for playing blackjack!")
    
        