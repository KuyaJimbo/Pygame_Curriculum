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
OBSTACLE_WIDTH = 40
OBSTACLE_HEIGHT = 60

# Create player
player = pygame.Rect(50, GROUND_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

# Player settings
is_jumping = False    
jump_speed = 15       
gravity = 1       
velocity_y = jump_speed

# Obstacles
obstacles = []
ground_obstacle_delay = random.randint(1000, 3000)
flying_obstacle_delay = random.randint(2000, 5000)
last_ground_obstacle = pygame.time.get_ticks()
last_flying_obstacle = pygame.time.get_ticks()

# Score and game over
score = 0
game_over = False

# Clock
clock = pygame.time.Clock()

def reset_game():
    global score, game_over, obstacles, player
    score = 0
    game_over = False
    obstacles = []
    player.y = GROUND_HEIGHT - PLAYER_HEIGHT

# Game loop
while True:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle game over and reset
    if game_over:
        font = pygame.font.SysFont(None, 55)
        game_over_text = font.render(f"Game Over! Score: {score}. Press SPACE to restart", True, RED)
        screen.blit(game_over_text, (100, HEIGHT // 2))
        pygame.display.flip()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            reset_game()
        clock.tick(60)
        continue

    # Player jump mechanics
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        velocity_y = -jump_speed

    if is_jumping:
        player.y += velocity_y
        velocity_y += gravity
        if player.y >= GROUND_HEIGHT - PLAYER_HEIGHT:
            player.y = GROUND_HEIGHT - PLAYER_HEIGHT
            is_jumping = False

    # Spawn ground obstacle
    current_time = pygame.time.get_ticks()
    if current_time - last_ground_obstacle > ground_obstacle_delay:
        obstacle = pygame.Rect(WIDTH, GROUND_HEIGHT - OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        obstacles.append(obstacle)
        last_ground_obstacle = current_time
        ground_obstacle_delay = random.randint(1000, 3000)

    # Spawn flying obstacle
    if current_time - last_flying_obstacle > flying_obstacle_delay:
        flying_obstacle = pygame.Rect(WIDTH, GROUND_HEIGHT - PLAYER_HEIGHT - 100, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
        obstacles.append(flying_obstacle)
        last_flying_obstacle = current_time
        flying_obstacle_delay = random.randint(2000, 5000)

    # Update obstacle positions and check for collision
    for obstacle in obstacles[:]:
        obstacle.x -= 5
        if player.colliderect(obstacle):
            game_over = True
        if obstacle.x + OBSTACLE_WIDTH < 0:
            obstacles.remove(obstacle)
            score += 1

    # Drawing
    screen.fill(WHITE)

    # Draw ground
    pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (WIDTH, GROUND_HEIGHT), 2)

    # Draw player
    pygame.draw.rect(screen, BLACK, player)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, GRAY, obstacle)

    # Draw score
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)
