#! python3

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for managing of bullet"""

    def __init__(self, ai_settings, screen, ship):
        """Create object bullet in actual position of ship"""
        super().__init__()
        self.screen = screen

        # Create bullet in point (0,0) and define position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top


        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moving bullet"""
        # Update position of bullet
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Display bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
