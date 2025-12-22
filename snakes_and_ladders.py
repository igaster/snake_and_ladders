from xmlrpc.client import Boolean

import pygame
import random
import sys

# Settings
CELL = 50 # Μέγεθος από κάθε τετράγωνο
dice = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)

# Initialize pygame
pygame.init()

class Ladder(object):
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def getType(self):
        if (self.start > self.end):
            return 'snake'
        else:
            return 'ladder'

    def get_color(self):
        if self.getType() == 'snake':
            return (255,0,0)
        else:
            return (0,255,0)


class Player(object):
    def __init__(self, name, position, color):
        self.name = name
        self.position = position
        self.color = color

ladders = [
    Ladder(7, 25),
    Ladder(32, 61),
    Ladder(45, 70),
    Ladder(88, 43),
]

players = [
    Player('red',  10, (255,0,0)),
    Player('green', 23, (0,255,0)),
    Player('blue', 78, (0,0,255)),
]

activePlayer = 0;

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Φιδάκια και Σκάλες")

# Font
font = pygame.font.SysFont(None, 32)

# Βοηθητική συνάρτηση δέχεται μία θέση του παιχνιδιού (1-100)
# και επιστρέφει τις συντεταγμένες (x,y) του κέντρου
def index_to_xy(index):
    index = index -1
    y = 9 - (index // 10)
    x = index % 10
    if y % 2 == 0:
        x = 9 - x
    return x * CELL + CELL // 2, y * CELL + CELL // 2

def draw_grid():
    for i in range(1, 11):
        pygame.draw.line(screen, BLACK, (i * CELL, 0), (i * CELL, 10 * CELL), 3)
        pygame.draw.line(screen, BLACK, (0, i * CELL), (10 * CELL, i * CELL), 3)

    for i in range(1, 101):
        text_surface = font.render(str(i), True, GRAY)
        text_rect = text_surface.get_rect(center=index_to_xy(i))
        screen.blit(text_surface, text_rect)

def draw_players():
    for player in players:
        pygame.draw.circle(screen, player.color, index_to_xy(player.position), 14)

def draw_ladders():
    for ladder in ladders:
        pygame.draw.line(screen, ladder.get_color(), index_to_xy(ladder.start), index_to_xy(ladder.end), 5)


def throw_dice():
    global players, activePlayer
    global dice
    dice = random.randint(1, 6)
    players[activePlayer].position += dice
    if players[activePlayer].position > 100:
        players[activePlayer].position = 100
    activePlayer = activePlayer + 1
    if activePlayer > len(players) - 1:
        activePlayer = 0

def winner() -> Player|Boolean:
    for player in players:
        if player.position == 100:
            return player
    return False

def draw_ui():
    text_surface = font.render("Dice:" + str(dice), True, BLACK)
    screen.blit(text_surface, (10, CELL * 10 + 10))
    if winner():
        text_surface = font.render("Player "+ winner().name + " wins", True, BLACK)
        screen.blit(text_surface, (10, CELL * 10 + 30))


# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Ελέγος αν πατήθηκε το πλήκτρο space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                throw_dice()
                print("Space Pressed")

    draw_grid()
    draw_ladders()
    draw_players()
    draw_ui()

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
    #
    # # Κείμενο
    # text_surface = font.render("Text", True, GRAY)
    # screen.blit(text_surface, (100, 100))

    pygame.display.flip()

pygame.quit()
sys.exit()