## Blackjack ##

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

from art import logo
import os
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

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif computer_score == 0:
        return "Blackjack for computer; You lose."
    elif user_score == 0:
        return "Blackjack! You win."
    elif user_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return "Computer went over 21. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

def play_blackjack():
    
    # print(logo)
    
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
        print(f"Computer's first card is {computer_cards[0]}.")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_end = True
        else:
            draw_card = input("Would you like to draw another card? Type 'yes' or 'no': ")
            if draw_card == 'yes':
                user_cards.append(deal_card())
            elif draw_card == 'no':
                game_end = True
        
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)    

    print(f"Your final hand: {user_cards}; Final Score: {user_score}.")
    print(f"Computer's final hand: {computer_cards}; Final Score: {computer_score}.")
    print(compare(user_score, computer_score))
    print("Thank you for playing!")
    print("")
    
while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': " ) == 'yes':
    os.system("cls" if os.name == "nt" else "clear")
    play_blackjack()

