# High or Low Game
# The High or Low game is a simple card game where the player guesses if the next card will be higher or lower than the previous card.
# The player wins if their guess is correct.

# Use import random to shuffle the deck of cards.
import random

# Create a dictionary to store the cards and their values.
card_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Ask the player how many times they want to play the game.
print('How many times do you want to play the game?')
times = int(input())
while times <= 0:
    print('Invalid number. How many times do you want to play the game?')
    times = int(input())

for play in range(times):
    # Create a deck of cards with their suits.
    deck = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
            '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
            '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
            '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥']

    # Shuffle the deck of cards.
    random.shuffle(deck)

    # Reveal a card from the deck.
    previous_card = deck.pop()
    print(f'Previous card: {previous_card}')

    # Ask the player if they think the next card will be higher or lower.
    print('Do you think the next card will be higher or lower? (higher or lower)')
    choice = input()
    while (choice != 'higher') and (choice != 'lower'):
        print('Invalid choice. Do you think the next card will be higher or lower? (higher or lower)')
        choice = input()

    # Reveal the next card from the deck.
    next_card = deck.pop()
    print(f'Next card: {next_card}')

    # Check if the player's choice is correct.
    previous_card_number = previous_card[:-1]
    previous_card_value = card_value[previous_card_number]
    next_card_number = next_card[:-1]
    next_card_value = card_value[next_card_number]

    if (choice == 'higher' and next_card_value > previous_card_value):
        print('You win!')
    elif (choice == 'lower' and next_card_value < previous_card_value):
        print('You win!')
    else:
        print('You lose!')