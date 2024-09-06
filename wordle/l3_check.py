
print("Welcome to Wordle!")

# Create a variable to store the answer
answer = "pizza"           

# Get the User's Guess
guess = input()             

# check if the guess is correct
if guess == answer:     # NEW
    print("You Win!")   # NEW
else:                   # NEW
    print("You Lose!")  # NEW