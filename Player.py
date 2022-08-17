import pygame
import random, sys
from os import path

img_dir = path.join(path.dirname("/Users/iriszhang/PycharmProjects/Pygame/SampleGame/"), "img")

pygame.init()
screen_width = 800
screen_height = 450
FPS = 60
ani = 4

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("First Game")
clock = pygame.time.Clock()


class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = brick_img
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image.set_colorkey(WHITE)
#        self.rect.centerx = screen_width / 2
     #   self.rect.bottom = screen_height - 10
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.health = 10
        self.score = 1
        self.images = []
        for i in range(1, 9):
            image = pygame.transform.scale(player_img, (40, 60))
            self.images.append(image)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        # moving left
        if self.movex < 0:
            self.frame += 1
            if self.frame > ani * 3:
                self.frame = 0
            self.image = self.images[self.frame//ani]

        # moving right
        if self.movex > 0:
            self.frame += 1
            if self.frame > ani*3:
                self.frame = 0
            self.image = self.images[(self.frame//ani)+4]
"""
        # collisions
        ground_hit_list = pygame.sprite.spritecollide(self,ground_list, False)
        for g in ground_hit_list:
            self.health -= 1
            print(self.health)

class Level():
    def ground(lvl, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                ground = Platform(gloc[i], screen_height-ty, tx, ty, "bricks.png")
                ground_list.add(ground)
                i = i+1
        if lvl ==2:
            print("Level" + str(lvl))
        return ground_list

    def platform(lvl, tx, ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        if lvl == 1:
            ploc.append(((0, screen_height-ty-128),3))
            ploc.append((300, screen_height-256,3))
            ploc.append((500, screen_height-ty-128,4))

            while i < len(ploc):
                j = 0
                while j <= ploc[i][2]:
                    plat = Platform((ploc[i][0] + (j * tx), ploc[i][1],tx,ty,"bricks.png"))
                    plat_list.add(plat)
                    j = j+1
                print("run" + str(i) + str(ploc[i]))
                i = i+1
        if lvl == 2:
            print("Level" + str(lvl))
        return plat_list
"""


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(coin_img, (40, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > screen_height + 10 or self.rect.left < -25 or self.rect.right > screen_width + 20:
            self.rect.x = random.randrange(screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Attack(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = attack_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > screen_height + 10 or self.rect.left < -25 or self.rect.right > screen_width + 20:
            self.rect.x = random.randrange(screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


# load all game graphics
background = pygame.image.load('bg.jpg').convert()
background_rect = background.get_rect()
player_img = pygame.image.load("sadboy.png").convert()
coin_img = pygame.image.load("coin.png").convert()
attack_img = pygame.image.load("bomb.png").convert()
brick_img = pygame.image.load("bricks.png").convert()


all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
attack = pygame.sprite.Group()
player = Player()
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10
all_sprites.add(player)

"""
gloc = []
tx = 64
ty = 64

i = 0
while i <= (screen_width/tx) + tx:
    gloc.append(i*tx)
    i = i+1

ground_list = Level.ground(1, gloc, tx, ty)
play_list = Level.platform(1, tx, ty)
"""

for i in range(8):
    c = Coin()
    all_sprites.add(c)
    coins.add(c)

for i in range(8):
    a = Attack()
    all_sprites.add(a)
    attack.add(a)

done = True
while done:
    # Process input (events)
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    # game logic starts from here
        if event.type == pygame.KEYDOWN:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                player.control(-steps, 0)
            if keystate[pygame.K_RIGHT]:
                player.control(steps, 0)
            if keystate[pygame.K_SPACE]:
                print("jump")
        if event.type == pygame.KEYUP:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                player.control(steps , 0)
            if keystate[pygame.K_RIGHT]:
                player.control(-steps, 0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                done = False

    # check to see if the coin hit the player
    hits = pygame.sprite.spritecollide(player, coins, False)
    hits2 = pygame.sprite.spritecollide(player, attack, False)
    #if hits or hits2:
        #done = False

    # clear/ reset the screen/ move to next level

    # set the background
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
 #   player_list.draw(screen)
#    play_list.draw(screen)
 #   ground_list.draw(screen)
    # set the fonts
    # drawing code starts
    # blitz function to load image

    # update the frame after drawing everything
    pygame.display.flip()
    # set the frame rate
    clock.tick(FPS)  # 60 frames/second

# quit pygame and clear window
pygame.QUIT  # like close.scanner in java
