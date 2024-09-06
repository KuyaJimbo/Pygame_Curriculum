import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 500
GRID_SIZE = 200

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Blindness Test")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 36)

# Game variables
score = 0
threshold = 50  # Initial threshold for color change
grid_rects = []
unique_cell = None
main_color = None
unique_color = None

# Functions to generate random colors and adjust them
def generate_color():
    return [random.randint(0, 255) for _ in range(3)]

def adjust_color(color, change):
    return [(c + change if c + change <= 255 else c - change) for c in color]

def generate_grid(threshold):
    global unique_cell, main_color, unique_color
    main_color = generate_color()
    unique_color = adjust_color(main_color, threshold)
    
    unique_cell = random.randint(0, 3)  # Random cell to be the unique one
    grid_rects.clear()
    
    for i in range(2):
        for j in range(2):
            rect = pygame.Rect(j * GRID_SIZE, i * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            grid_rects.append(rect)

# Draw grid with colors
def draw_grid():
    for idx, rect in enumerate(grid_rects):
        color = unique_color if idx == unique_cell else main_color
        pygame.draw.rect(screen, color, rect)

# Draw score
def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, HEIGHT - 40))

# Game loop
def game_loop():
    global score, threshold
    
    running = True
    generate_grid(threshold)

    while running:
        screen.fill(WHITE)

        draw_grid()
        draw_score()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Reset game
                    score = 0
                    threshold = 50
                    generate_grid(threshold)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for idx, rect in enumerate(grid_rects):
                    if rect.collidepoint(pos):
                        if idx == unique_cell:
                            score += 1
                            threshold = max(1, threshold - 5)  # Decrease threshold slightly
                        else:
                            score = 0  # Reset score on wrong click
                            threshold = 50
                        generate_grid(threshold)

        pygame.display.flip()

# Run the game
game_loop()
pygame.quit()
