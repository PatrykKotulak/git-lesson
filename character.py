#! python3

import pygame
from PIL import I

class Character():
    """Prepare character"""

    def __init__(self, screen):
        """Inicjalization character"""
        self.screen = screen

        # Download and prepare image to load
        self.image = pygame.image.load('images\\computer-games-787176_1920.bmp')
        self.image = pygame.transform.scale(self.image, (300, 150))
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Place where character is
        self.image_rect.bottom = self.screen_rect.bottom
        self.image_rect.centerx = self.screen_rect.centerx

    def blit_character(self):
        """Appear character"""
        self.screen.blit(self.image, self.image_rect)



