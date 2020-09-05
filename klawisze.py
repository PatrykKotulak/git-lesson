#! python3

import pygame

def run():

    pygame.init()
    screen = pygame.display.set_mode((1600, 800))


    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)

    pygame.display.flip()

run()