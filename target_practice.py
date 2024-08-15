import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Target Shooting Game")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Define target properties
TARGET_RADIUS = 50
TARGET_COLORS = [RED, BLUE, GREEN]

# Initialize score and high score
score = 0
high_score = 0

# Game states
WAITING = 0
PLAYING = 1
GAME_OVER = 2
game_state = WAITING

# Timer
GAME_TIME = 20000  # 20 seconds in milliseconds
start_time = 0

# Function to create a new target
def create_target():
    x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
    y = random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS)
    return (x, y)

# Create initial target
target_pos = create_target()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_state != PLAYING:
                # Start the game
                game_state = PLAYING
                score = 0
                start_time = pygame.time.get_ticks()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_state == PLAYING:
            # Check if mouse click is within the target
            mouse_pos = pygame.mouse.get_pos()
            distance = ((mouse_pos[0] - target_pos[0]) ** 2 + (mouse_pos[1] - target_pos[1]) ** 2) ** 0.5
            
            if distance <= TARGET_RADIUS:
                # Calculate score based on distance from center
                if distance <= TARGET_RADIUS / 3:
                    score += 10  # Center: 10 points
                elif distance <= 2 * TARGET_RADIUS / 3:
                    score += 5   # Middle ring: 5 points
                else:
                    score += 3   # Outer ring: 3 points
                
                # Create a new target
                target_pos = create_target()

    # Clear the screen
    screen.fill(WHITE)

    if game_state == WAITING:
        # Display "Press SPACE to start" message
        font = pygame.font.Font(None, 36)
        start_text = font.render("Press SPACE to start", True, BLACK)
        text_rect = start_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(start_text, text_rect)

    elif game_state == PLAYING:
        # Calculate remaining time
        elapsed_time = pygame.time.get_ticks() - start_time
        remaining_time = max(0, (GAME_TIME - elapsed_time) // 1000)

        if remaining_time == 0:
            game_state = GAME_OVER
            high_score = max(high_score, score)

        # Draw the target
        pygame.draw.circle(screen, TARGET_COLORS[0], target_pos, TARGET_RADIUS)
        pygame.draw.circle(screen, TARGET_COLORS[1], target_pos, 2 * TARGET_RADIUS // 3)
        pygame.draw.circle(screen, TARGET_COLORS[2], target_pos, TARGET_RADIUS // 3)

        # Display the timer
        font = pygame.font.Font(None, 36)
        timer_text = font.render(f"Time: {remaining_time}s", True, BLACK)
        screen.blit(timer_text, (WIDTH - 150, 10))

    elif game_state == GAME_OVER:
        # Display "Game Over" message
        font = pygame.font.Font(None, 48)
        game_over_text = font.render("Game Over", True, BLACK)
        text_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(game_over_text, text_rect)

        # Display "Press SPACE to restart" message
        font = pygame.font.Font(None, 36)
        restart_text = font.render("Press SPACE to restart", True, BLACK)
        text_rect = restart_text.get_rect(center=(WIDTH/2, HEIGHT/2 + 50))
        screen.blit(restart_text, text_rect)

    # Display the score and high score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    high_score_text = font.render(f"High Score: {high_score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()