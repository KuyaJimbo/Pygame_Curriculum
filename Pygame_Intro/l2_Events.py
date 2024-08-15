import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Keep track of the game state
run = True

# Game loop
while run:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # other event types include
        # pygame.KEYDOWN
        # pygame.KEYUP
        # pygame.MOUSEBUTTONDOWN
        # pygame.MOUSEBUTTONUP
        # pygame.MOUSEMOTION

        if event.type == pygame.KEYDOWN:
            print("Key pressed")

pygame.quit()