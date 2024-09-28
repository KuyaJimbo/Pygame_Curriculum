# Monty Hall Problem:
# There are 3 doors, behind one of them is a car, behind the other two are goats.
# The player picks a door, and then the host opens one of the other two doors to reveal a goat.
# The player can then choose to switch to the other unopened door, or stay with their original choice.
# The player wins the car if they choose the door with the car behind it.
# The player loses if they choose a door with a goat behind it.
# The player can win or lose by switching or staying.

# Use a dictionary to store the doors and their contents.
doors = {1: 'goat', 2: 'goat', 3: 'car'}

# Ask the player to pick a door.
print('Pick a door: 1, 2, or 3')

# Validate the player's choice.
player_pick = int(input())
while player_pick not in doors:
    print('Invalid choice. Pick a door: 1, 2, or 3')
    player_pick = int(input())

# The host opens one of the other two doors to reveal a goat.
# The host can choose randomly or strategically.
if player_pick == 1:
    if doors[2] == 'goat':
        host_open = 3
    else:
        host_open = 2
elif player_pick == 2:
    if doors[1] == 'goat':
        host_open = 3
    else:
        host_open = 1
else:
    if doors[1] == 'goat':
        host_open = 2
    else:
        host_open = 1

# Print the host's choice.
print(f'The host opens door {host_open} to reveal a goat.')

# Ask the player if they want to switch doors.
print('Do you want to switch doors? (yes or no)')
switch = input()
while (switch != 'yes') and (switch != 'no'):
    print('Invalid choice. Do you want to switch doors? (yes or no)')
    switch = input()

# The player switches doors.
if switch == 'yes':
    if player_pick == 1:
        if host_open == 2:
            player_pick = 3
        else:
            player_pick = 2
    elif player_pick == 2:
        if host_open == 1:
            player_pick = 3
        else:
            player_pick = 1
    else:
        if host_open == 1:
            player_pick = 2
        else:
            player_pick = 1

# Print the player's final choice.
print(f'You choose door {player_pick}.')
# Print the contents of each door.
for door, contents in doors.items():
    print(f'Door {door}: {contents}')

# Determine if the player wins or loses.
if doors[player_pick] == 'car':
    print('You win!')
else:
    print('You lose!')