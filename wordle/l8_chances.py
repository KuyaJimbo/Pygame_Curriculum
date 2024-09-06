
print("Welcome to Wordle!")

# Create a variable to store the answer
answer = "pizza"

# Create a variable to store the number of guesses
chances = 6     # NEW

for chance in range(chances):
    # Get the User's Guess
    guess = input()

    for index in range(0, 5):           
        answer_letter = answer[index]
        guess_letter = guess[index]     

        if guess_letter == answer_letter:   
            print(answer_letter, end="")    
        elif guess_letter in answer:        
            print("?", end="")              
        else:                               
            print("_", end="")
        
    # Create a new line
    print()