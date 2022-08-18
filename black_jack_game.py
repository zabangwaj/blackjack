import random
from art import logo
print (logo)
still_playing = True

cards = 4 * ["ace",2,3,4,5,6,7,8,9,10,10,10,10]
random.shuffle(cards)

your_cards = [cards[0], cards[2]]
computer_cards = [cards[1], cards[3]]
card_count = 4

def get_card(old_cards):
    global card_count
    old_cards.append(cards[card_count])
    card_count += 1
    return (old_cards)

def calculate_score(the_cards):
    score = 0
    count_ace = 0
    for card in the_cards:
        if card == "ace":
            count_ace += 1
            score += 11
        else:
            score += card
    if score > 21 and count_ace > 0:
        while (count_ace > 0) and (score > 21):
            score -= 10
            count_ace -= 1
    else:
        return score
    return score

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 21:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 21:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    elif computer_score > user_score:
        return "Lose, opponent has more points than you 😱"

print (f"Your cards are: {your_cards}")
print (f"Your score is: {calculate_score(your_cards)}")
print (f"The computer's first card is: {computer_cards[0]}")

while still_playing:
    get_another_card = input ("Type 'y' to get another card, type 'n' to pass: ")
    if get_another_card == 'y':
        get_card(your_cards)
        print (f"Your cards: {your_cards}, current score: {calculate_score(your_cards)}")
        if calculate_score(your_cards) > 21:
            still_playing = False
    elif get_another_card == 'n':
        while (21 > calculate_score(your_cards) > calculate_score(computer_cards)):
            get_card(computer_cards)
        still_playing = False

print ("The End!")
print(compare (calculate_score(your_cards), calculate_score(computer_cards)))
print (f"Your cards: {your_cards}")
print (f"Oponent's Cards: {computer_cards}")