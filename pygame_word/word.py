import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
FONT_SIZE = 40
FONT = pygame.font.Font(None, FONT_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (169, 169, 169)

# Game variables
word_to_guess = "codes"  # The answer
max_guesses = 6          # Number of guesses allowed
word_length = len(word_to_guess)

# Dynamic screen size based on word length and number of guesses
width = word_length * FONT_SIZE * 2
height = max_guesses * (FONT_SIZE + 10)
screen = pygame.display.set_mode((width, height))

# Function to draw text on the screen
def draw_text(text, color, x, y):
    rendered_text = FONT.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Function to check each guess
def check_guess(guess, answer):
    result = []
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            result.append(GREEN)
        elif guess[i] in answer:
            result.append(YELLOW)
        else:
            result.append(GRAY)
    return result

# Main game loop
guesses = []
current_guess = ""
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                current_guess = current_guess[:-1]  # Remove last letter
            elif event.key == pygame.K_RETURN and len(current_guess) == word_length:
                guesses.append(current_guess)
                current_guess = ""
                if len(guesses) == max_guesses or guesses[-1] == word_to_guess:
                    running = False
            elif len(current_guess) < word_length:
                current_guess += event.unicode

    # Draw guesses on the screen
    for i, guess in enumerate(guesses):
        colors = check_guess(guess, word_to_guess)
        for j, letter in enumerate(guess):
            draw_text(letter.upper(), colors[j], j * (FONT_SIZE + 10), i * (FONT_SIZE + 10))

    # Draw current guess
    for j, letter in enumerate(current_guess):
        draw_text(letter.upper(), BLACK, j * (FONT_SIZE + 10), len(guesses) * (FONT_SIZE + 10))

    pygame.display.flip()

# End game screen
screen.fill(WHITE)
if guesses[-1] == word_to_guess:
    draw_text("You win!", GREEN, width // 4, height // 2)
else:
    draw_text("You lose!", BLACK, width // 4, height // 2)
pygame.display.flip()

# Wait for a few seconds before closing
pygame.time.wait(3000)
pygame.quit()
