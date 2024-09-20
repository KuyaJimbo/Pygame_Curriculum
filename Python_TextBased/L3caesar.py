# Create dictionaries for mapping numbers to letters and vice versa
number_to_letter = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e",
                    5: "f", 6: "g", 7: "h", 8: "i", 9: "j",
                    10: "k", 11: "l", 12: "m", 13: "n", 14: "o",
                    15: "p", 16: "q", 17: "r", 18: "s", 19: "t",
                    20: "u", 21: "v", 22: "w", 23: "x", 24: "y",
                    25: "z"}

letter_to_number = {value: key for key, value in number_to_letter.items()}

# Split the input by spaces and process each "step!message"
words = input("Enter input (e.g., '3!you 4!solved 5!the'): ").split()

# Loop through each word in the format "step!message"
for word in words:
    step_message = word.split("!")
    step = int(step_message[0])  # Extract step
    message = step_message[1]  # Extract the message

    encoded_message = ""

    # Apply Caesar cipher for each letter in the message
    for letter in message:
        if letter == " ":  # Keep spaces unchanged
            encoded_message += " "
        else:
            number = letter_to_number[letter]  # Convert letter to number
            new_number = (number + step) % 26  # Perform Caesar cipher shift
            new_letter = number_to_letter[new_number]  # Convert number back to letter
            encoded_message += new_letter  # Append to the result

    # Print the result in the format "step!encoded_message"
    print(f"{step}!{encoded_message}", end=" ")
