import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack-a-Mole")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game settings
TARGET_SIZE = 50
TARGET_SPAWN_TIME = 1000  # in milliseconds
GAME_DURATION = 30  # in seconds

# Font for score display
font = pygame.font.Font(None, 36)

class Target:
    def __init__(self):
        self.x = random.randint(TARGET_SIZE, WIDTH - TARGET_SIZE)
        self.y = random.randint(TARGET_SIZE, HEIGHT - TARGET_SIZE)
        self.spawn_time = pygame.time.get_ticks()

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), TARGET_SIZE)
        pygame.draw.circle(screen, WHITE, (self.x, self.y), TARGET_SIZE - 10)
        pygame.draw.circle(screen, RED, (self.x, self.y), TARGET_SIZE // 2)

def calculate_score(click_pos, target):
    distance = math.sqrt((click_pos[0] - target.x)**2 + (click_pos[1] - target.y)**2)
    if distance <= TARGET_SIZE:
        return max(0, int(100 - (distance / TARGET_SIZE) * 100))
    return 0

def main():
    clock = pygame.time.Clock()
    score = 0
    targets = []
    game_start_time = pygame.time.get_ticks()

    while True:
        current_time = pygame.time.get_ticks()
        time_left = max(0, GAME_DURATION - (current_time - game_start_time) // 1000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for target in targets[:]:
                    points = calculate_score(event.pos, target)
                    if points > 0:
                        score += points
                        targets.remove(target)

        # Spawn new targets
        if current_time % TARGET_SPAWN_TIME < 100 and len(targets) < 5:
            targets.append(Target())

        # Remove old targets
        targets = [target for target in targets if current_time - target.spawn_time < 2000]

        # Drawing
        screen.fill(BLACK)
        for target in targets:
            target.draw()

        # Display score and time left
        score_text = font.render(f"Score: {score}", True, WHITE)
        time_text = font.render(f"Time: {time_left}s", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (WIDTH - 150, 10))

        pygame.display.flip()

        # Check if game is over
        if time_left == 0:
            game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(3000)  # Wait for 3 seconds before quitting
            pygame.quit()
            sys.exit()

        clock.tick(60)

if __name__ == "__main__":
    main()