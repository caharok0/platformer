import pygame
from levels import *
from objects import *

pygame.init()

player = Player(50, H - 90, 40, 50, 10, player_images)

level1_objects, key, dungeon = draw_level(level1)
level1_objects.add(player)



game = True
while game:

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
        is_key = True
        key.rect.x =- 200

    if pygame.sprite.collide_rect(player, dungeon) and is_key:
        coins_count += 100
        dungeon.rect.x = -300



    pygame.display.update()
    clock.tick(FPS)
