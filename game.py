import pygame
from objects import *

pygame.init()

game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(bg, (0, 0))
    pygame.display.update()
    clock.tick(FPS)
