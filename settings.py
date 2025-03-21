import pygame

pygame.init()

W, H = 1280, 700
FPS = 20
coins_count = 0
is_key = False

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Platformer")
pygame.display.set_icon(pygame.image.load("assets/images/player/stand_1.png"))

clock = pygame.time.Clock()
'''ГРУПИ СПРАЙТІВ'''
platforms = pygame.sprite.Group()
coins = pygame.sprite.Group()
'''КАРТИНКИ СПРАЙТІВ'''
bg = pygame.transform.scale(pygame.image.load("assets/background/CB (1).jpg"), (W, H))

platform_image = pygame.image.load("assets/background/chess-pattern-8061034_1280.jpg")

player_images = [
    pygame.image.load("assets/images/player/stand_1.png"),
    pygame.image.load("assets/images/player/stand_2.png"),
    pygame.image.load("assets/images/player/stand_3.png"),
    pygame.image.load("assets/images/player/stand_4.png"),
    pygame.image.load("assets/images/player/move_right_1.png"),
    pygame.image.load("assets/images/player/move_right_2.png"),
    pygame.image.load("assets/images/player/move_right_3.png"),
    pygame.image.load("assets/images/player/move_right_4.png"),
    pygame.image.load("assets/images/player/move_right_5.png"),
    pygame.image.load("assets/images/player/move_right_6.png"),
    pygame.image.load("assets/images/player/move_left_1.png"),
    pygame.image.load("assets/images/player/move_left_2.png"),
    pygame.image.load("assets/images/player/move_left_3.png"),
    pygame.image.load("assets/images/player/move_left_4.png"),
    pygame.image.load("assets/images/player/move_left_5.png"),
    pygame.image.load("assets/images/player/move_left_6.png"),
]

coin_image = pygame.image.load("assets/images/coin/coin-removebg-preview.png")
dungeon_image = pygame.image.load("assets/images/dungeon/dungeon (1).png")
key_image = pygame.image.load("assets/images/key/key.png")
portal_image = pygame.image.load("assets/images/portal/portal.png")




'''ШРИФТИ'''
pygame.font.init()
font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 60)

'''ТЕКСТИ'''
find_key_txt = font2.render("Знайти ключ", True, (255, 155, 255))
open_dungeon_txt = font2.render("натисни e щоб відкрити", True, (255, 155, 255))
get_key_txt = font2.render("натисни e щоб підібрати", True, (255, 155, 255))