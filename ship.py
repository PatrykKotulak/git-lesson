#! python3
from pygame.sprite import Sprite
import pygame

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Inicjalization ship and its position"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # Loadind image and download its rectangle
        self.image = pygame.image.load('images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # New ship appear at the bottom picture
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Point of center in float
        self.center = float(self.rect.centerx)

        # moving ship
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update position ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Display of ship space in actual position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Places ship on center"""
        self.center = self.screen_rect.centerx