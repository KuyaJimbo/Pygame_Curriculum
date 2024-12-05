import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower Defense: Tower Mechanics")

# Color Palette
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 150, 255)
YELLOW = (255, 255, 0)
GRAY = (150, 150, 150)

# Projectile Class
class Projectile:
    def __init__(self, x, y, target, damage):
        """
        Create a projectile fired by a tower
        
        Parameters:
        - x: Starting x-position of the tower
        - y: Starting y-position of the tower
        - target: Enemy the projectile is targeting
        - damage: Amount of damage the projectile will do
        """
        self.x = x
        self.y = y
        self.target = target
        self.damage = damage
        self.speed = 5
        self.color = YELLOW

    def move(self):
        """
        Move the projectile towards the target
        """
        # Calculate direction to target
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        
        # Calculate distance
        distance = math.sqrt(dx**2 + dy**2)
        
        # Normalize and move
        if distance > 0:
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

    def draw(self, screen):
        """
        Draw the projectile
        """
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)

    def is_hit_target(self):
        """
        Check if projectile has hit the target
        """
        dx = self.x - self.target.x
        dy = self.y - self.target.y
        return math.sqrt(dx**2 + dy**2) < 10

# Tower Class with Advanced Mechanics
class Tower:
    def __init__(self, x, y, tower_type):
        """
        Create a tower with specific characteristics
        
        Parameters:
        - x: Tower's x-position
        - y: Tower's y-position
        - tower_type: Determines tower's capabilities
        """
        self.x = x
        self.y = y
        self.tower_type = tower_type
        self.size = 40
        self.projectiles = []
        
        # Tower type configurations
        self.configs = {
            'basic': {
                'color': LIGHT_BLUE,
                'damage': 10,
                'range': 150,
                'fire_rate': 30,  # Lower is faster
                'cost': 50
            },
            'sniper': {
                'color': BLUE,
                'damage': 50,
                'range': 300,
                'fire_rate': 60,
                'cost': 100
            },
            'splash': {
                'color': RED,
                'damage': 20,
                'range': 100,
                'fire_rate': 45,
                'cost': 75
            }
        }
        
        # Set tower attributes based on type
        self.config = self.configs[tower_type]
        self.fire_cooldown = 0

    def find_target(self, enemies):
        """
        Find the closest enemy within range
        """
        closest_enemy = None
        closest_distance = float('inf')
        
        for enemy in enemies:
            dx = self.x - enemy.x
            dy = self.y - enemy.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance <= self.config['range'] and distance < closest_distance:
                closest_enemy = enemy
                closest_distance = distance
        
        return closest_enemy

    def shoot(self, enemies):
        """
        Attempt to shoot at an enemy
        """
        # Increment cooldown
        self.fire_cooldown += 1
        
        # Check if ready to fire
        if self.fire_cooldown >= self.config['fire_rate']:
            target = self.find_target(enemies)
            
            if target:
                # Create projectile
                projectile = Projectile(
                    self.x + self.size // 2, 
                    self.y + self.size // 2, 
                    target, 
                    self.config['damage']
                )
                self.projectiles.append(projectile)
                
                # Reset cooldown
                self.fire_cooldown = 0

    def update_projectiles(self, enemies):
        """
        Update and manage projectiles
        """
        projectiles_to_remove = []
        
        for projectile in self.projectiles:
            projectile.move()
            
            # Check for hits
            if projectile.is_hit_target():
                # Damage enemy based on tower type
                if self.tower_type == 'splash':
                    # Splash damage affects nearby enemies
                    for enemy in enemies:
                        if (math.sqrt((projectile.x - enemy.x)**2 + 
                                      (projectile.y - enemy.y)**2) < 50):
                            enemy.take_damage(projectile.damage)
                else:
                    # Normal damage
                    projectile.target.take_damage(projectile.damage)
                
                projectiles_to_remove.append(projectile)
        
        # Remove hit projectiles
        for proj in projectiles_to_remove:
            self.projectiles.remove(proj)

    def draw(self, screen):
        """
        Draw the tower and its range
        """
        # Draw tower base
        pygame.draw.rect(screen, self.config['color'], 
                         (self.x, self.y, self.size, self.size))
        
        # Draw range (optional - for visualization)
        pygame.draw.circle(screen, (*self.config['color'], 100), 
                           (self.x + self.size // 2, self.y + self.size // 2), 
                           self.config['range'], 1)
        
        # Draw projectiles
        for projectile in self.projectiles:
            projectile.draw(screen)

    def is_clicked(self, mouse_pos):
        """
        Check if tower is clicked
        """
        mx, my = mouse_pos
        return (self.x <= mx <= self.x + self.size and 
                self.y <= my <= self.y + self.size)

# Enemy Class (simplified from previous lesson)
class Enemy:
    def __init__(self, x, y, health, speed, color):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.speed = speed
        self.color = color
        self.radius = 20

    def move(self):
        self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Health bar
        health_width = self.radius * 2
        health_height = 5
        health_bar_x = int(self.x - health_width / 2)
        health_bar_y = int(self.y - self.radius - 10)
        
        pygame.draw.rect(screen, RED, (health_bar_x, health_bar_y, health_width, health_height))
        current_health_width = int(health_width * (self.health / self.max_health))
        pygame.draw.rect(screen, GREEN, (health_bar_x, health_bar_y, current_health_width, health_height))

    def take_damage(self, damage):
        self.health -= damage
        return damage

# Main Game Loop
clock = pygame.time.Clock()
running = True

# Game state
score = 0
money = 200  # Starting money

# Lists for game objects
enemies = []
towers = []

# Tower placement mode
placing_tower = None

while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Tower placement
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # Check tower type selection
            if 10 <= mouse_pos[0] <= 110:
                if 50 <= mouse_pos[1] <= 100:
                    # Basic tower selected
                    if money >= 50:
                        placing_tower = 'basic'
                elif 150 <= mouse_pos[1] <= 200:
                    # Sniper tower selected
                    if money >= 100:
                        placing_tower = 'sniper'
                elif 250 <= mouse_pos[1] <= 300:
                    # Splash tower selected
                    if money >= 75:
                        placing_tower = 'splash'
            
            # Place tower
            elif placing_tower:
                new_tower = Tower(mouse_pos[0] - 20, mouse_pos[1] - 20, placing_tower)
                towers.append(new_tower)
                
                # Deduct money
                money -= new_tower.config['cost']
                placing_tower = None
    
    # Spawn enemies
    if random.randint(1, 30) == 1:
        new_enemy = Enemy(
            x=SCREEN_WIDTH,
            y=random.randint(50, SCREEN_HEIGHT - 50),
            health=50,
            speed=-2,
            color=GRAY
        )
        enemies.append(new_enemy)
    
    # Update enemies
    for enemy in enemies[:]:
        enemy.move()
        
        # Remove enemies that go off screen
        if enemy.x < 0:
            enemies.remove(enemy)
            continue
    
    # Tower mechanics
    for tower in towers:
        tower.shoot(enemies)
        tower.update_projectiles(enemies)
    
    # Remove dead enemies
    enemies = [enemy for enemy in enemies if enemy.health > 0]
    
    # Drawing
    # Draw side menu for tower selection
    pygame.draw.rect(screen, GRAY, (0, 0, 120, SCREEN_HEIGHT))
    
    # Draw tower selection buttons
    pygame.draw.rect(screen, LIGHT_BLUE, (10, 50, 100, 50))  # Basic Tower
    pygame.draw.rect(screen, BLUE, (10, 150, 100, 50))       # Sniper Tower
    pygame.draw.rect(screen, RED, (10, 250, 100, 50))        # Splash Tower
    
    # Draw all game objects
    for enemy in enemies:
        enemy.draw(screen)
    
    for tower in towers:
        tower.draw(screen)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
