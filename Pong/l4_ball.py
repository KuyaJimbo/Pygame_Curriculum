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
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
PADDLE_SPEED = 5

# Create game objects
left_player = pygame.Rect(50, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_player = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball settings
BALL_SIZE = 15      # NEW
BALL_SPEED_X = 3    # NEW
BALL_SPEED_Y = 3    # NEW

# Create ball object
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE) # NEW

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the left_player's paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_player.top > 0:
        left_player.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_player.bottom < HEIGHT:
        left_player.y += PADDLE_SPEED

    if keys[pygame.K_UP] and right_player.top > 0:
        right_player.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_player.bottom < HEIGHT:
        right_player.y += PADDLE_SPEED

    # Move the ball
    ball.x += BALL_SPEED_X # NEW
    ball.y += BALL_SPEED_Y # NEW

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_player)
    pygame.draw.rect(screen, WHITE, right_player)
    pygame.draw.ellipse(screen, WHITE, ball) # NEW

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)