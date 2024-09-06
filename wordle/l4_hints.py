
print("Welcome to Wordle!")

# Create a variable to store the answer
answer = "pizza"         

# Get the User's Guess
guess = input()             

# check if the guess is correct
if guess == answer:     
    print("You Win!")   
else:                   
    print("You Lose!")  

# use a FOR LOOP to give hints
for letter in answer:               # NEW
    if letter in guess:             # NEW
        print(letter, end = " ")    # NEW
    else:                           # NEW      
        print("_", end = " ")       # NEW