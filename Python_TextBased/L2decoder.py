translation = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}

#reverse_translation = {value: key for key, value in translation.items()}

reverse_translation = {}

for key, value in translation.items():
    reverse_translation[value] = key

message = input()

for i in range(len(message)):
    letter = message[i]
    if letter in reverse_translation:
        print(reverse_translation[letter], end="")
    else:
        print(letter, end="")