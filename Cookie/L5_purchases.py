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
        self.x = x
        self.y = y
        self.radius = radius
        self.value = value

    def draw(self):
        pygame.draw.circle(screen, BROWN, (self.x, self.y), self.radius)
        

    def clicked(self, pos):
        return ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) ** 0.5 <= self.radius

# Create the cookie object: Cookie(CenterX, CenterY, Radius, Value)                       
cookie = Cookie(WIDTH // 2, HEIGHT // 2, 50, 1)

# Upgrade Class
class Upgrade:
    # What does an upgrade need?
    def __init__(self, x, y, width, height, name, price, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.price = price
        self.value = value
        self.quantity = 0

    def draw(self):
        pygame.draw.rect(screen, LIGHT_GRAY, (self.x, self.y, self.width, self.height))
        screen.blit(font.render(f"{self.name}: {self.quantity}", True, BLACK), (self.x + 10, self.y + 10))
        screen.blit(font.render(f"Price: {self.price}", True, BLACK), (self.x + 10, self.y + 40))
        screen.blit(font.render(f"Value: {self.value}/s", True, BLACK), (self.x + 10, self.y + 70))

    def clicked(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height
    
    def purchase(self, cookies):                    # NEW
        print("Purchase " + self.name)              # NEW
        # if we have more cookies than the price    # NEW
            # increase the quantity by 1            # NEW
            # increase the price by 15%             # NEW
            # return True                           # NEW
        # else                                      # NEW
            # print "Not enough cookies"            # NEW
            # return False                          # NEW


# Create an upgrade object: Upgrade(x, y, width, height, name, price, value)
factory = Upgrade(WIDTH - 220, 220, 200, 100, "Factory", 50, 5)
grandma = Upgrade(WIDTH - 220, 100, 200, 100, "Grandma", 10, 1)

# Game Variables
total_cookies = 0
cookies_per_second = 0
clock = pygame.time.Clock()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("Mouse Clicked")
            # Check if the cookie was clicked
            if cookie.clicked(event.pos):
                # add the cookie's value to the total_cookies
                total_cookies += cookie.value
            # Check if the upgrade was clicked
            if factory.clicked(event.pos):
                # if the upgrade was purchased
                if factory.purchase(total_cookies):
                    # subtract the price from the cookies
                    total_cookies -= factory.price
                    # increase the quantity by 1
                    cookies_per_second += factory.value

    screen.fill(WHITE)
    # Draw the Cookie
    cookie.draw()
    # Draw the Upgrade
    factory.draw()

    screen.blit(font.render(f"Cookies: {int(total_cookies)}", True, BLACK), (10, 10))
    screen.blit(font.render(f"Per second: {cookies_per_second}", True, BLACK), (10, 50))

    pygame.display.flip()
    clock.tick(60) # 60 FPS (Frames Per Second)