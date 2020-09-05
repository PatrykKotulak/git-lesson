#! python3

import pygame
from PIL import Image

class Size_Image():
    """Change size image"""

    def __init__(self):
        self.image_im = Image.open('images\\486c34cf5b3b4badd52bc'
                                   '427dbeb44a1-rocket-cartoon-by-vexels.png')
        self.im_width, self.im_height = self.image_im.size

    def change_size(self, settings):
        if self.im_width > settings.max_size_image or self.im_height > \
                settings.max_size_image:
            if self.im_width > self.im_height:
                self.im_height = int((settings.max_size_image / self.im_width)
                                     * self.im_height)
                self.im_width = settings.max_size_image
            else:
                self.im_width = int((settings.max_size_image / self.im_height)
                                    * self.im_width)
                self.im_height = settings.max_size_image



class Rocket_Image():
    """Inicjalization rocket"""

    def __init__(self, screen, settings):

        self.screen = screen
        self.settings = settings

        # Match size image
        size_image = Size_Image()
        size_image.change_size(settings)


        self.image = pygame.image.load('images\\486c34cf5b3b4badd52bc427db'
                                       'eb44a1-rocket-cartoon-by-vexels.png')
        self.image = pygame.transform.scale(self.image, (size_image.im_width,
                                                         size_image.im_height))

        #Change image to rect
        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.image_rect.center = self.screen_rect.center

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.centerx += self.settings.speed_rocket
        if self.move_left and self.image_rect.right > 0:
            self.image_rect.centerx -= self.settings.speed_rocket
        if self.move_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.bottom += self.settings.speed_rocket
        if self.move_up and self.image_rect.top > 0:
            self.image_rect.bottom -= self.settings.speed_rocket

    def blit_rocket(self):
        self.screen.blit(self.image, self.image_rect)