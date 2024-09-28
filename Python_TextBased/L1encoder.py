translation = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}

message = input()

for i in range(len(message)):
    letter = message[i]
    if letter in translation:
        print(translation[letter], end="")
    else:
        print(letter, end="")

# Input: you encoded the message
# Output: y45 2nc4d2d th2 m2ss1g2


