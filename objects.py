from settings import *

#клас обєктів мапи
class MapObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#клас який спадкуєця
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, heigth, speed, images):
        super().__init__()
        self.width = width
        self.heigth = heigth
        self.images = images #список картинок
        self.anim_count = 0 #номер анімації
        self.image = pygame.transform.scale(self.images[self.anim_count], (width, heigth))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#клас для гравця
class Player(Sprite):
    def __init__(self, x, y, width, heigth, speed, images):
        super().__init__(x, y, width, heigth, speed, images)

        self.action = "idle" #дія гравця (поточна)
        self.animations = { #номери анімацій в залежності від дій гравця
            "idle": list(range(4)),
            "right": list(range(4, 10)),
            "left": list(range(10, 17))
        }

        self.is_jump = False
        self.jump_count = 25

        self.fall = 0
        self.gravity = 2
        self.on_ground = False
    
    def update(self, platforms): # оновлення гравця
        frames = self.animations[self.action]#[0, 1, 2, 3] # номери анімації в залежності від дії гравця
        self.anim_count += 1 #перемикаємо анімацію
        if self.anim_count >= len(frames) - 1:
            self.anim_count = 0 # обнуляємо номер анімації коли вони закінчуюця
        self.image = pygame.transform.scale(self.images[frames[self.anim_count]], (self.width, self.heigth))

        self.fall += self.gravity
        self.rect.y += self.fall
        hit_platforms  = pygame.sprite.spritecollide(self, platforms, False)
        if hit_platforms:
            for plarform in hit_platforms:
                if self.fall > 0 and self.rect.bottom > plarform.rect.top:
                    self.rect.bottom = plarform.rect.top
                    self.fall = 0
                    self.on_ground = True
        else:
            self.on_ground = False

        keys_pressed = pygame.key.get_pressed()# рух в ліво
        if keys_pressed[pygame.K_a]:
            self.action = "left"
            self.rect.x -= self.speed
        elif keys_pressed[pygame.K_d]: # рух в право
            self.action = "right"
            self.rect.x += self.speed
        else:
            self.action = "idle" #без руху

        if not self.is_jump:
            if keys_pressed[pygame.K_SPACE]:
                if self.on_ground:
                    self.is_jump = True
                    self.fall -= self.jump_count
        else:
            self.is_jump = not self.on_ground