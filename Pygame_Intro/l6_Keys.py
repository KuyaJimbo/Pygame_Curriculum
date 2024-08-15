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

    # keep track of the keys pressed
    keys = pygame.key.get_pressed()
        
    # Move the kid based on the keys pressed
    if keys[pygame.K_LEFT]:
        kid_x -= 0.1
    
    if keys[pygame.K_RIGHT]:
        kid_x += 0.1
    
    if keys[pygame.K_UP]:
        kid_y -= 0.1
    
    if keys[pygame.K_DOWN]:
        kid_y += 0.1

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the display
    pygame.display.update()

pygame.quit()