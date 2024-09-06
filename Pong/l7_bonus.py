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
BALL_SIZE = 15
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Create ball object
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

# Scores
left_score = 0      # NEW
right_score = 0     # NEW
winning_score = 3   # NEW

# Font for score display
font = pygame.font.Font(None, 74)   # NEW

# Game loop
clock = pygame.time.Clock()

def reset_ball():
    ball.x = WIDTH // 2 - BALL_SIZE // 2
    ball.y = HEIGHT // 2 - BALL_SIZE // 2
    global BALL_SPEED_X
    BALL_SPEED_X = 3

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
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Ball collision with paddles
    if ball.colliderect(left_player) or ball.colliderect(right_player):
        BALL_SPEED_X = -BALL_SPEED_X

    # Check if a player scored
    if ball.left <= 0:
        right_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()

    # LAST PIECE OF THE CODE: Check if someone wins
    if left_score >= winning_score or right_score >= winning_score:
        winner_text = "Left Player Wins!" if left_score >= winning_score else "Right Player Wins!"
        winner_surface = font.render(winner_text, True, WHITE)
        screen.fill(BLACK)
        screen.blit(winner_surface, (WIDTH // 2 - winner_surface.get_width() // 2, HEIGHT // 2 - winner_surface.get_height() // 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_player)
    pygame.draw.rect(screen, WHITE, right_player)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw center line
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Display the score
    left_score_surface = font.render(str(left_score), True, WHITE)
    right_score_surface = font.render(str(right_score), True, WHITE)
    screen.blit(left_score_surface, (WIDTH // 4 - left_score_surface.get_width() // 2, 20))
    screen.blit(right_score_surface, (3 * WIDTH // 4 - right_score_surface.get_width() // 2, 20))

    # Update the display
    pygame.display.flip()

    # increase the speed of the ball
    BALL_SPEED_X += 0.01 # NEW

    # Control the game speed
    clock.tick(60)
