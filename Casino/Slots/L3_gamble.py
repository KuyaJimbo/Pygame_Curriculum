# Slot Machine Game
# There are 3 slots, each with 3 possible symbols: cherry, lemon, and orange.
# The player can pull the lever to spin the slots.
# If all 3 slots have the same symbol, the player wins the jackpot.
import random

# Use a dictionary to store the slots and their symbols.
slots = ['cherry', 'lemon', 'orange']

# Create a Jackpot Value                                 # NEW
jackpots = {'cherry': 100, 'lemon': 50, 'orange': 25}    # NEW

# Ask the player if they want to play the slots.
print('Do you want to play the slots? (yes or no)')
choice = input()
while True:
    
    if choice == 'yes':
        break
    elif choice == 'no':
        print('Goodbye!')
        exit()
    else:
        print('Invalid choice. Do you want to play the slots? (yes or no)')
        choice = input()
        continue
    

    # Spin the slots.
    slot1 = random.choice(slots)
    slot2 = random.choice(slots)
    slot3 = random.choice(slots)

    # Print the slots.
    print(f'Slots: {slot1} {slot2} {slot3}')

    # Check if the player wins the jackpot.
    if slot1 == slot2 == slot3:
        print("Jackpot! You win", jackpots[slot1])      # NEW   
    else:
        print("Try again next time.")

