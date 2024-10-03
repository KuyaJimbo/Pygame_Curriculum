import pygame
import sys

# Setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)
LIGHT_GRAY = (200, 200, 200)

# Cookie Class
class Cookie:
    def __init__(self, x, y, radius, value):
        # create cookie's x, y, radius, and value
        pass

    def draw(self):
        # pygame.draw.circle(screen, COLOR, (x, y), radius)
        pass

    def clicked(self, pos):
        return ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) ** 0.5 <= self.radius

# Create the cookie object                          # NEW
# cookie = Cookie(CenterX, CenterY, Radius, Value)  # NEW

# Game Variables
total_cookies = 0
cookies_per_second = 0
clock = pygame.time.Clock()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("Mouse Clicked")

 
    screen.fill(WHITE)

    # Draw the Cookie   # NEW
    # cookie.draw()     # NEW

    screen.blit(font.render(f"Cookies: {int(total_cookies)}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Per second: {cookies_per_second}", True, BLACK), (10, 50))

    pygame.display.flip()
    clock.tick(60) # 60 FPS (Frames Per Second)