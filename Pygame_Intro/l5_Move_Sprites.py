import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the image of the kid
kid = pygame.image.load("kid.png").convert_alpha()

# Initial position of the kid
kid_x = 100
kid_y = 100

# Keep track of the game state
run = True

# Game loop
while run:

    # Fill the screen with dark grey
    screen.fill((50, 50, 50))

    # Draw the kid image at the current position
    screen.blit(kid, (kid_x, kid_y))

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Move kid to the left by 10 pixels
                kid_x -= 10

            if event.key == pygame.K_RIGHT:
                # Move kid to the right by 10 pixels
                kid_x += 10

            if event.key == pygame.K_UP:
                # Move kid up by 10 pixels
                kid_y -= 10

            if event.key == pygame.K_DOWN:
                # Move kid down by 10 pixels
                kid_y += 10

    # Update the display
    pygame.display.update()

pygame.quit()
