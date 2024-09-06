import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Keep track of the game state
run = True

# Load the sound file
coin_sound = pygame.mixer.Sound('coin.wav')

# Game loop
while run:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            print("Key pressed")
            # play the sound when a key is pressed
            coin_sound.play() 
            

        if event.type == pygame.KEYUP:
            print("Key released")

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse button pressed")
            # create a new rectangle at the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (255, 0, 0), (mouse_x, mouse_y, 50, 50))
        
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse button released")
            # create a new circle at the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0, 255, 0), (mouse_x, mouse_y), 25)


        if event.type == pygame.MOUSEMOTION:
            print("Mouse moved")
            # change the background to blue
            screen.fill((0, 0, 255))
        else:
            # change the background to white
            screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

pygame.quit()