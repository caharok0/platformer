import pygame
from levels import *
from objects import *

pygame.init()

level1_objects, key, dungeon = draw_level(level1)
player = Player(50, H - 90, 40, 50, 10, player_images)
portal = MapObject(1100, 480, 80, 80,  portal_image)


level1_objects.add(player)
level1_objects.add(portal)

key_pressed = pygame.key.get_pressed()
game = True
while game:

    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(bg, (0, 0))
    for obj in level1_objects:
        window.blit(obj.image, camera.apply(obj))
    camera.update(player)

    player.update(platforms)

    if pygame.sprite.spritecollide(player, coins, True):
        coins_count += 1

    window.blit(pygame.transform.scale(coin_image, (70, 40)), (1, 10))
    coin_txt = font1.render(f": {coins_count}", True, (255, 255, 255))
    window.blit(coin_txt, (55, 15))

    if pygame.sprite.collide_rect(player, key):
        window.blit(get_key_txt, (W//2, 50))
        if key_pressed[pygame.K_e]:
            is_key = True
            key.rect.x =- 300

    if pygame.sprite.collide_rect(player, dungeon) and is_key:
        window.blit(open_dungeon_txt, (W//2, 50))
        if key_pressed[pygame.K_e]:
            coins_count += 100
            dungeon.rect.x = -300

    if pygame.sprite.collide_rect(player, dungeon) and not is_key:
        window.blit(get_key_txt, (W//2, 50))

    pygame.display.update()
    clock.tick(FPS)
