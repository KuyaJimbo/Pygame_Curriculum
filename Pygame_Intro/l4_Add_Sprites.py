import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Keep track of the game state
run = True

# add image of kid.png with convert_alpha() method
kid = pygame.image.load("kid.png").convert_alpha()

# Game loop
while run:

    # Fill the screen with dark grey
    screen.fill((50, 50, 50))

    # Draw the kid image
    screen.blit(kid, (100, 100))

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the display
    pygame.display.update()

pygame.quit()