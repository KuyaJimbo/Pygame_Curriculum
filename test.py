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

# Keeping Score
font = pygame.font.Font(None, 36)                           # NEW
score = 0                                                   # NEW
score_text = font.render(f"Score: {score}", True, WHITE)    # NEW

# Ship Settings
ship_width = 20         
ship_height = 30        
ship_x = WIDTH // 2     
ship_y = HEIGHT - 100   
ship_speed = 5          

# Create the Ship game object
ship = pygame.Rect(ship_x, ship_y, ship_width, ship_height)  

# Bullet Settings
bullet_radius = 5
bullet_speed = 7

# Create the Bullet game object
bullet = None
# Keep track of the bullets
bullets = []

# Asteroid Settings
asteroid_width = 30     
asteroid_height = 30    
asteroid_speed = 2      

# Create the Asteroid game object
asteroid = None           
# Keep track of the asteroids
asteroids = []            

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new bullet
                bullet = pygame.Rect(ship.x + ship.width // 2, ship.y, bullet_radius, bullet_radius)
                bullets.append(bullet)
            if event.key == pygame.K_0:
                # Choose a random position
                randomX = random.randint(0, WIDTH - asteroid_width)                   
                # Create a new asteroid
                asteroid = pygame.Rect(randomX, 0, asteroid_width, asteroid_height)   
                asteroids.append(asteroid)                                            

    # Move the bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        # Remove bullets that go off-screen
        if bullet.y < 0:            
            bullets.remove(bullet)  
        
    # Move the asteroids
    for asteroid in asteroids:        
        asteroid.y += asteroid_speed
        # Remove asteroids that go off-screen
        if asteroid.y > HEIGHT:         
            asteroids.remove(asteroid)  

    # Get user input
    keys = pygame.key.get_pressed()

    # Check for collisions between bullets and asteroids
    for bullet in bullets[:]:                     # Loop through bullets
        for asteroid in asteroids[:]:             # Loop through asteroids
            if bullet.colliderect(asteroid):      # Check if they collide
                bullets.remove(bullet)            # Remove bullet
                asteroids.remove(asteroid)        # Remove asteroid
                break                             # Break out of the asteroid loop

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
    for bullet in bullets:
        pygame.draw.circle(screen, WHITE, (bullet.x, bullet.y), bullet_radius)
        
    # Draw the asteroids:
    for asteroid in asteroids:                    
        pygame.draw.rect(screen, RED, asteroid)

    # Draw the score text
    pygame.draw.rect(screen, BLACK, (0, 0, 100, 50))            # NEW
    score_text = font.render(f"Score: {score}", True, WHITE)    # NEW
    screen.blit(score_text, (10, 10))                           # NEW

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(60)