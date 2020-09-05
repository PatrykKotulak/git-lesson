#! python3

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class representing alien"""

    def __init__(self, ai_settings, screen):
        """Inicjalization alien"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loadind image and download its rectangle
        self.image = pygame.image.load('images\\alien.bmp')
        self.rect = self.image.get_rect()


        # New ship appear at the bottom picture
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Point of center in float
        self.x = float(self.rect.x)

    def blitme(self):
        """Display of alien in actual position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien touch edges"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Movement right and left"""
        self.x += (self.ai_settings.alien_speed_factor *
                  self.ai_settings.fleet_direction)
        self.rect.x = self.x