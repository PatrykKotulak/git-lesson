#! python3

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Inicjalization game and create screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('Inwazja obcych')

    play_button = Button(ai_settings, screen, 'Gra')


    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)


    # Create space ship
    ship = Ship(ai_settings, screen)
    # Create group to store of bullet
    bullets = Group()
    aliens = Group()

    # Create fleet of alien
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Beginning main loop of game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullet(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens,
                             bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)

        #showing last modified screen
        pygame.display.flip()

run_game()