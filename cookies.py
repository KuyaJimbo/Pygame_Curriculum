import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BROWN = (139, 69, 19)

# Game variables
cookies = 0
cookies_per_click = 1
cookies_per_second = 0

# Upgrade buttons
click_upgrades = [
    {"name": "Cursor", "cost": 15, "increase": 1},
    {"name": "Grandma", "cost": 100, "increase": 5},
    {"name": "Farm", "cost": 1100, "increase": 8},
]

cps_upgrades = [
    {"name": "Auto-Clicker", "cost": 50, "increase": 1},
    {"name": "Bakery", "cost": 500, "increase": 5},
    {"name": "Factory", "cost": 3000, "increase": 10},
]

# Font
font = pygame.font.Font(None, 24)

def draw_cookie():
    pygame.draw.circle(screen, BROWN, (WIDTH // 2, HEIGHT // 2), 100)

def draw_counter():
    text = font.render(f"Cookies: {int(cookies)}", True, BLACK)
    screen.blit(text, (10, 10))
    
    cps_text = font.render(f"CPS: {cookies_per_second}", True, BLACK)
    screen.blit(cps_text, (10, 40))

def draw_upgrades():
    for i, upgrade in enumerate(click_upgrades):
        pygame.draw.rect(screen, GRAY, (WIDTH - 200, 100 + i * 60, 180, 50))
        name_text = font.render(upgrade["name"], True, BLACK)
        cost_text = font.render(f"Cost: {upgrade['cost']}", True, BLACK)
        screen.blit(name_text, (WIDTH - 190, 105 + i * 60))
        screen.blit(cost_text, (WIDTH - 190, 125 + i * 60))

    for i, upgrade in enumerate(cps_upgrades):
        pygame.draw.rect(screen, GRAY, (20, 100 + i * 60, 180, 50))
        name_text = font.render(upgrade["name"], True, BLACK)
        cost_text = font.render(f"Cost: {upgrade['cost']}", True, BLACK)
        screen.blit(name_text, (30, 105 + i * 60))
        screen.blit(cost_text, (30, 125 + i * 60))

def check_upgrades(pos):
    global cookies, cookies_per_click, cookies_per_second

    for i, upgrade in enumerate(click_upgrades):
        if WIDTH - 200 <= pos[0] <= WIDTH - 20 and 100 + i * 60 <= pos[1] <= 150 + i * 60:
            if cookies >= upgrade["cost"]:
                cookies -= upgrade["cost"]
                cookies_per_click += upgrade["increase"]
                upgrade["cost"] = int(upgrade["cost"] * 1.15)

    for i, upgrade in enumerate(cps_upgrades):
        if 20 <= pos[0] <= 200 and 100 + i * 60 <= pos[1] <= 150 + i * 60:
            if cookies >= upgrade["cost"]:
                cookies -= upgrade["cost"]
                cookies_per_second += upgrade["increase"]
                upgrade["cost"] = int(upgrade["cost"] * 1.15)

# Main game loop
clock = pygame.time.Clock()
last_second = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                if (x - WIDTH // 2) ** 2 + (y - HEIGHT // 2) ** 2 <= 100 ** 2:
                    cookies += cookies_per_click
                check_upgrades((x, y))

    # Update cookies based on CPS
    current_time = pygame.time.get_ticks()
    if current_time - last_second >= 1000:
        cookies += cookies_per_second
        last_second = current_time

    # Draw everything
    screen.fill(WHITE)
    draw_cookie()
    draw_counter()
    draw_upgrades()

    pygame.display.flip()
    clock.tick(60)