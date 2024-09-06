import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors Simulation")

# Colors
LIGHT_ORANGE = (255, 200, 100)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Object class
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, obj_type):
        super().__init__()
        self.obj_type = obj_type
        self.speed = 2
        self.angle = random.uniform(0, 2 * math.pi)
        self.dx = self.speed * math.cos(self.angle)
        self.dy = self.speed * math.sin(self.angle)

        if obj_type == "rock":
            self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(self.image, GRAY, (10, 10), 10)
        elif obj_type == "paper":
            self.image = pygame.Surface((20, 20))
            self.image.fill(WHITE)
        else:  # scissors
            self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.polygon(self.image, BLUE, [(10, 0), (20, 20), (0, 20)])

        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Bounce off walls
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.dy *= -1

    def transform(self, new_type):
        self.obj_type = new_type
        if new_type == "rock":
            self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(self.image, GRAY, (10, 10), 10)
        elif new_type == "paper":
            self.image = pygame.Surface((20, 20))
            self.image.fill(WHITE)
        else:  # scissors
            self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.polygon(self.image, BLUE, [(10, 0), (20, 20), (0, 20)])

# Create sprite group and objects
all_sprites = pygame.sprite.Group()

for _ in range(10):
    all_sprites.add(Object(random.randint(0, WIDTH), random.randint(0, HEIGHT), "rock"))
    all_sprites.add(Object(random.randint(0, WIDTH), random.randint(0, HEIGHT), "paper"))
    all_sprites.add(Object(random.randint(0, WIDTH), random.randint(0, HEIGHT), "scissors"))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Check for collisions
    for sprite in all_sprites:
        collided = pygame.sprite.spritecollide(sprite, all_sprites, False)
        for other in collided:
            if sprite != other:
                # Change direction after collision
                sprite.angle = random.uniform(0, 2 * math.pi)
                sprite.dx = sprite.speed * math.cos(sprite.angle)
                sprite.dy = sprite.speed * math.sin(sprite.angle)

                # Transform based on rock-paper-scissors rules
                if sprite.obj_type == "rock" and other.obj_type == "paper":
                    sprite.transform("paper")
                elif sprite.obj_type == "paper" and other.obj_type == "scissors":
                    sprite.transform("scissors")
                elif sprite.obj_type == "scissors" and other.obj_type == "rock":
                    sprite.transform("rock")

    # Draw
    screen.fill(LIGHT_ORANGE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()