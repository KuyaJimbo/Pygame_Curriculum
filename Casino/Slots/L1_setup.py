# Slot Machine Game
# There are 3 slots, each with 3 possible symbols: cherry, lemon, and orange.
# The player can pull the lever to spin the slots.
# If all 3 slots have the same symbol, the player wins the jackpot.
import random

# Use a dictionary to store the slots and their symbols.
slots = ['cherry', 'lemon', 'orange']

# Ask the player to pull the lever.
print('Pull the lever to spin the slots. (press enter)')
input()

# Spin the slots.
slot1 = random.choice(slots)
slot2 = random.choice(slots)
slot3 = random.choice(slots)

# Print the slots.
print(f'Slots: {slot1} {slot2} {slot3}')

# Check if the player wins the jackpot.
if slot1 == slot2 == slot3:
    print("Jackpot! You win!")
else:
    print("Try again next time.")