import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Galaga")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Ship Settings
ship_width = 20         # NEW
ship_height = 30        # NEW
ship_x = WIDTH // 2     # NEW
ship_y = HEIGHT - 100   # NEW
ship_speed = 5          # NEW

# Create the Ship game object
ship = pygame.Rect(ship_x, ship_y, ship_width, ship_height)  # NEW

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get user input
    keys = pygame.key.get_pressed()

    # Move the ship
    if keys[pygame.K_LEFT]:     # NEW
        ship.x -= ship_speed    # NEW
    if keys[pygame.K_RIGHT]:    # NEW
        ship.x += ship_speed    # NEW

    # Draw the screen
    screen.fill(BLACK)

    # Draw the ship's hull
    pygame.draw.rect(screen, WHITE, ship) # NEW

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)