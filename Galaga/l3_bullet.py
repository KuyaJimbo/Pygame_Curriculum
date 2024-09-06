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
ship_width = 20         
ship_height = 30        
ship_x = WIDTH // 2     
ship_y = HEIGHT - 100   
ship_speed = 5          

# Create the Ship game object
ship = pygame.Rect(ship_x, ship_y, ship_width, ship_height)  

# Bullet Settings
bullet_radius = 5       # NEW
bullet_speed = 7        # NEW

# Create the Bullet game object
bullet = None           # NEW
# Keep track of the bullets
bullets = []            # NEW

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:        # NEW
            if event.key == pygame.K_SPACE:     # NEW
                # Create a new bullet
                bullet = pygame.Rect(ship.x + ship.width // 2, ship.y, bullet_radius, bullet_radius)    # NEW
                bullets.append(bullet)          # NEW

    # Move the bullets
    for bullet in bullets:          # NEW
        bullet.y -= bullet_speed    # NEW

    # Get user input
    keys = pygame.key.get_pressed()

    # Move the ship
    if keys[pygame.K_LEFT]:     
        ship.x -= ship_speed    
    if keys[pygame.K_RIGHT]:    
        ship.x += ship_speed    

    # Draw the screen
    screen.fill(BLACK)

    # Draw the ship's hull
    pygame.draw.rect(screen, WHITE, ship)

    # Draw the bullets
    for bullet in bullets:                                                        # NEW
        pygame.draw.circle(screen, WHITE, (bullet.x, bullet.y), bullet_radius)    # NEW

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)