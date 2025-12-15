import pygame
import random
import sys

# Settings
CELL = 50

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

    for i in range(1, 11):
        pygame.draw.line(screen, BLACK, (i * CELL, 0), (i * CELL, 500), 3)
        pygame.draw.line(screen, BLACK, (0, i * CELL), (500, i * CELL), 3)

    # # Γραμμή
    # pygame.draw.line(screen, BLACK, (100, 100), (600, 100), 3)
    #
    # # Ορθογώνιο, μόνο περίγραμμα
    # pygame.draw.rect(screen, BLACK, (30, 30, 40, 80), 1)
    #
    # # Ορθογώνιο, με γέμισμα
    # pygame.draw.rect(screen, BLACK, (130, 120, 40, 80))


    pygame.display.flip()

pygame.quit()
sys.exit()