number_to_letter = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e",
                    5: "f", 6: "g", 7: "h", 8: "i", 9: "j",
                    10: "k", 11: "l", 12: "m", 13: "n", 14: "o",
                    15: "p", 16: "q", 17: "r", 18: "s", 19: "t",
                    20: "u", 21: "v", 22: "w", 23: "x", 24: "y",
                    25: "z"}

letter_to_number = {value: key for key, value in number_to_letter.items()}

message = input()
step = int(input())

for i in range(len(message)):
    if letter == " ":
        print(" ", end="")
        continue
    letter = message[i]
    number = letter_to_number[letter]
    new_number = (number + step) % 26 
    new_letter = number_to_letter[new_number]
    print(new_letter, end="")

# input: wklv hqfubsw ira wkh vhfuhw
# input: 3
# output: you solved the caesar cipher