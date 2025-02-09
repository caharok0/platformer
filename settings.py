import pygame

pygame.init()

W, H = 1280, 700
FPS = 20

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Platformer")
pygame.display.set_icon(pygame.image.load("assets/images/player/stand_1.png"))

clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load("assets/background/level1.png"), (W, H))