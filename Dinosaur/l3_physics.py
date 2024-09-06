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
GROUND_HEIGHT = 350
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

# OBSTACLE_WIDTH = 20
# OBSTACLE_HEIGHT = 40
# SPEED = 5

# Create player
player = pygame.Rect(50, GROUND_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

# Player settings
is_jumping = False      # NEW
jump_speed = 15         # NEW

# # Obstacle settings
# obstacle = pygame.Rect(WIDTH, GROUND_HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
# obstacle_speed = SPEED

# # Score
# score = 0
# font = pygame.font.Font(None, 36)

# Clock
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player jump mechanics
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True

    if is_jumping:
        
        

    # # Move the obstacle
    # obstacle.x -= obstacle_speed

    # # Check if obstacle is off-screen and reset its position
    # if obstacle.right < 0:
    #     obstacle.x = WIDTH
    #     score += 1  # Increase score as player avoids obstacle

    # # Collision detection
    # if player.colliderect(obstacle):
    #     game_over_surface = font.render("Game Over!", True, RED)
    #     screen.fill(BLACK)
    #     screen.blit(game_over_surface, (WIDTH // 2 - game_over_surface.get_width() // 2, HEIGHT // 2))
    #     pygame.display.flip()
    #     pygame.time.delay(2000)
    #     pygame.quit()
    #     sys.exit()

    # Drawing
    screen.fill(WHITE)

    # Draw ground
    pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (WIDTH, GROUND_HEIGHT), 2)

    # Draw player
    pygame.draw.rect(screen, BLACK, player)

    # # Draw obstacle
    # pygame.draw.rect(screen, BLACK, obstacle)

    # # Display the score
    # score_surface = font.render(f"Score: {score}", True, BLACK)
    # screen.blit(score_surface, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)
