#! python3

import pygame
from rocket_settings import Settings
from rocket_image import Rocket_Image
import rocket_game_functions as rgf
import sys

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption('Rocket')
    rocket = Rocket_Image(screen, settings)

    while True:

        screen.fill(settings.bg_color)

        rgf.check_key(rocket)
        rocket.update()
        rocket.blit_rocket()
        pygame.display.flip()

run_game()