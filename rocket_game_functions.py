#! python3

import pygame
import sys

def press_key(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.move_right = True
    if event.key == pygame.K_UP:
        rocket.move_up = True
    if event.key == pygame.K_LEFT:
        rocket.move_left = True
    if event.key == pygame.K_DOWN:
        rocket.move_down = True

def release_key(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.move_right = False
    if event.key == pygame.K_UP:
        rocket.move_up = False
    if event.key == pygame.K_LEFT:
        rocket.move_left = False
    if event.key == pygame.K_DOWN:
        rocket.move_down = False

def check_key(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            press_key(event, rocket)
        elif event.type == pygame.KEYUP:
            release_key(event, rocket)