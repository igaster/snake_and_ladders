import pygame
import random
import sys

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Φιδάκια και Σκάλες")

# Font
font = pygame.font.SysFont(None, 48)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if space was pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space Precces")

    screen.fill(WHITE)

    # Γραμμή
    pygame.draw.line(screen, BLACK, (1, 1), (100, 100), 3)

    # Ορθογώνιο, μόνο περίγραμμα
    pygame.draw.rect(screen, BLACK, (30, 30, 40, 80), 1)

    # Ορθογώνιο, με γέμισμα
    pygame.draw.rect(screen, BLACK, (130, 120, 40, 80))


    pygame.display.flip()

pygame.quit()
sys.exit()