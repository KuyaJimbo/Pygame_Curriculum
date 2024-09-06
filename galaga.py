import pygame
import random

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

# Ship class
class Ship:
    def __init__(self):
        self.width = 20
        self.height = 30
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.speed = 5

    def draw(self):
        pygame.draw.polygon(screen, WHITE, [
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height),
            (self.x + self.width // 2, self.y)
        ])

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.radius = 5
        self.x = x
        self.y = y
        self.speed = 7

    def move(self):
        self.y -= self.speed

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

# Enemy class
class Enemy:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = random.randint(0, WIDTH - self.width)
        self.y = 0
        self.speed = 2

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Game variables
ship = Ship()
bullets = []
enemies = []
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(ship.x + ship.width // 2, ship.y))
            elif event.key == pygame.K_e:
                enemies.append(Enemy())

    # Move ship
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.x -= ship.speed
    if keys[pygame.K_RIGHT]:
        ship.x += ship.speed

    # Move bullets and check collisions
    for bullet in bullets[:]:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)
        for enemy in enemies[:]:
            if (enemy.x < bullet.x < enemy.x + enemy.width and
                enemy.y < bullet.y < enemy.y + enemy.height):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Move enemies and check collisions
    for enemy in enemies[:]:
        enemy.move()
        if enemy.y + enemy.height > HEIGHT:
            enemies.remove(enemy)
        if (ship.x < enemy.x + enemy.width and
            ship.x + ship.width > enemy.x and
            ship.y < enemy.y + enemy.height and
            ship.y + ship.height > enemy.y):
            running = False

    # Draw everything
    screen.fill(BLACK)
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, HEIGHT - 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()