import pygame
import random
import sys

# Settings
CELL = 50 # Μέγεθος από κάθε τετράγωνο

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Φιδάκια και Σκάλες")

# Font
font = pygame.font.SysFont(None, 24)

# Βοηθητική συνάρτηση δέχεται μία θέση του παιχνιδιού (1-100)
# και επιστρέφει τις συντεταγμένες (x,y) του κέντρου
def index_to_grid(index):
    index = index -1
    y = 9 - (index // 10)
    x = index % 10
    if y % 2 == 0:
        x = 9 - x
    return x * CELL + CELL // 2, y * CELL + CELL // 2

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Ελέγος αν πατήθηκε το πλήκτρο space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space Pressed")

    screen.fill(WHITE)

    for i in range(1, 11):
        pygame.draw.line(screen, BLACK, (i * CELL, 0), (i * CELL, 10 * CELL), 3)
        pygame.draw.line(screen, BLACK, (0, i * CELL), (10 * CELL, i * CELL), 3)

    for i in range(1, 101):
        text_surface = font.render(str(i), True, GRAY)
        text_rect = text_surface.get_rect(center=index_to_grid(i))
        screen.blit(text_surface, text_rect)

    # # Γραμμή
    # pygame.draw.line(screen, BLACK, (100, 100), (600, 100), 3)
    #
    # # Ορθογώνιο, μόνο περίγραμμα
    # pygame.draw.rect(screen, BLACK, (30, 30, 40, 80), 1)
    #
    # # Ορθογώνιο, με γέμισμα
    # pygame.draw.rect(screen, BLACK, (130, 120, 40, 80))
    #
    # # Κύκλος
    # pygame.draw.circle(screen, BLACK, (100, 100), 14,  1)

    pygame.display.flip()

pygame.quit()
sys.exit()