import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the game window  
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Runner")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game settings
GROUND_HEIGHT = 350  # NEW
PLAYER_WIDTH = 40    # NEW
PLAYER_HEIGHT = 60   # NEW

# Create player
player = pygame.Rect(50, GROUND_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT) # NEW

# Clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Drawing
    screen.fill(WHITE)

    # Draw ground
    pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (WIDTH, GROUND_HEIGHT), 2) # NEW

    # Draw player
    pygame.draw.rect(screen, BLACK, player) # NEW

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)
