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

        if event.type == pygame.KEYDOWN:
            print("Key pressed")

        if event.type == pygame.KEYUP:
            print("Key released")

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse button pressed")
        
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse button released")

        if event.type == pygame.MOUSEMOTION:
            print("Mouse moved")

pygame.quit()