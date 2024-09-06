
print("Welcome to Wordle!")

# Create a variable to store the answer
answer = "pizza"          

# Get the User's Guess
guess = input()             

# HOW DOES A STRING WORK?
# A string is a sequence of characters
# Each character has an index

#          0 1 2 3 4
# answer = P I Z Z A

# answer[0] = P
# answer[1] = I
# answer[2] = Z
# answer[3] = Z
# answer[4] = A
# answer[5] = IndexError

for index in range(0, 5):           # NEW
    answer_letter = answer[index]   # NEW
    print(answer_letter)            # NEW