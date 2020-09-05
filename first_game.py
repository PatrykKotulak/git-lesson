#! python3

import sys
import pygame
from character import Character

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))
    pygame.display.set_caption('First game')

    while True:

        screen.fill((0, 50, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        character = Character(screen)
        character.blit_character()
        pygame.display.flip()

run_game()