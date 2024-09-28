# BlackJack
import random

# Create a dictionary to store the cards and their values.
card_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Create a deck of cards with their suits.
deck = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
        '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
        '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
        '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥']

# Shuffle the deck of cards.
random.shuffle(deck)

# Initialize the player's and dealer's hands.
player_hand = []
dealer_hand = []

# Deal the first two cards to the player and dealer.
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# Initialize the player's and dealer's scores.
player_score = 0
dealer_score = 0

# Calculate the player's score.
for card in player_hand:
    player_score += card_value[card[:-1]]

# Calculate the dealer's score.
for card in dealer_hand:
    dealer_score += card_value[card[:-1]]

# Print the player's and dealer's hands and scores.
print(f'Player hand: {player_hand} ({player_score})')
print(f'Dealer hand: {dealer_hand} ({dealer_score})')

# Ask the player if they want to hit or stand.
print('Do you want to hit or stand? (hit or stand)')
choice = input()
while (choice != 'hit') and (choice != 'stand'):
    print('Invalid choice. Do you want to hit or stand? (hit or stand)')
    choice = input()

    # The player hits.
    if choice == 'hit':
        player_hand.append(deck.pop())
        player_score += card_value[player_hand[-1][:-1]]
        print(f'Player hand: {player_hand} ({player_score})')
        print(f'Dealer hand: {dealer_hand} ({dealer_score})')
        choice = input()
    else:
        break

# The dealer hits if their score is less than 17.
while dealer_score < 17:
    dealer_hand.append(deck.pop())
    dealer_score += card_value[dealer_hand[-1][:-1]]
    print(f'Player hand: {player_hand} ({player_score})')
    print(f'Dealer hand: {dealer_hand} ({dealer_score})')

# Determine the winner.
if player_score > 21:
    print('Player busts. Dealer wins.')
elif dealer_score > 21:
    print('Dealer busts. Player wins.')
elif player_score > dealer_score:
    print('Player wins.')
elif player_score < dealer_score:
    print('Dealer wins.')
else:
    print('It\'s a tie.')
