import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH = 15   # NEW
PADDLE_HEIGHT = 90  # NEW
PADDLE_SPEED = 5    # NEW

# Create game objects
left_player = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) # NEW

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the left_player's paddle
    keys = pygame.key.get_pressed()                         # NEW
    if keys[pygame.K_w] and left_player.top > 0:            # NEW
        left_player.y -= PADDLE_SPEED                       # NEW
    if keys[pygame.K_s] and left_player.bottom < HEIGHT:    # NEW
        left_player.y += PADDLE_SPEED                       # NEW

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_player) # NEW

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)