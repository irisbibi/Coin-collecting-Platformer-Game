import pygame
import random

# initialize pygame
pygame.init()
screen_width = 800
screen_height = 450
FPS = 54

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#  Set up the display
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Don't get Crashed!")
clock = pygame.time.Clock()

# Loading graphics
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
attack_img = pygame.image.load("arrow.jpg")
attack_img = pygame.transform.scale(attack_img, (40, 40))

# instance variables
score = 0
hp = 4
ADD_NEW_BOMB_RATE = 50


class Player(object):  # movement
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hitbox = (self.x, self.y, 64, 64)
        self.health = 10
        self.visible = True

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(char, (self.x, self.y))
     # pygame.draw.rect(screen, RED, (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
     # pygame.draw.rect(screen, GREEN,(self.hitbox[0], self.hitbox[1] - 20, 50 - ((50 / 10) * (10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 10, 30, 54)

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            game_over()


class Cannon:
    cannon_velocity = 3

    def __init__(self, boolean):
        self.cannon_img = pygame.image.load("cannon.png")
        self.cannon_img = pygame.transform.scale(self.cannon_img, (50, 50))
        self.cannon_img_rect = self.cannon_img.get_rect()
        self.cannon_img_rect.width -= 10
        self.cannon_img_rect.height -= 10
        self.cannon_img_rect.top = 0
        self.cannon_img_rect.right = screen_width / 2
        self.right = boolean
        self.left = not boolean

    # move left and right within the screen
    def update(self):
        screen.blit(self.cannon_img, self.cannon_img_rect)
        if self.cannon_img_rect.right >= screen_width:
            self.left = True
            self.right = False
        elif self.cannon_img_rect.left <= 0:
            self.right = True
            self.left = False
        if self.right:
            self.cannon_img_rect.right += self.cannon_velocity
        elif self.left:
            self.cannon_img_rect.left -= self.cannon_velocity


class Bombs:
    bombs_velocity = 10

    # follow the cannon
    def __init__(self, Cannon):
        self.bombs_img = pygame.image.load("bomb.png")
        # self.bombs_img = pygame.transform.scale(self.bombs_img, (30, 30))
        self.bombs_img_rect = self.bombs_img.get_rect()
        self.bombs_img_rect.left = Cannon.cannon_img_rect.left
        self.bombs_img_rect.top = Cannon.cannon_img_rect.bottom

    # move down the screen
    def update(self):
        screen.blit(self.bombs_img, self.bombs_img_rect)
        if self.bombs_img_rect.bottom > 0:
            self.bombs_img_rect.bottom += self.bombs_velocity


class Brick(object):
    def __init__(self, pos, f):
        bricks.append(self)
        self.brick_img = pygame.transform.scale(pygame.image.load("platform.png"), (f, 80))
        self.brick_img_rect = self.brick_img.get_rect()
        self.brick_img_rect = pygame.Rect(pos[0], pos[1], f, 80)
        screen.blit(self.brick_img, self.brick_img_rect)


def game_over():
    game_over_img = pygame.image.load("end.jpg")
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(game_over_img, game_over_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            if event.type == pygame.KEYDOWN:
                done = False
                    # sys.exit()
                # game_loop()
        pygame.display.flip()


def redrawGameWindow():
    # screen.blit(bg, (0,0))
    text = font.render("Score: " + str(score), 1, BLACK)
    text1 = font.render("Level: " + str(level), 1, BLACK)
    player.draw(screen)
    screen.blit(text, (600, 10))
    screen.blit(text1, (600, 40))
    pygame.display.flip()

    # pygame.draw.rect(screen, RED, [x, y, width, height], 0)
    # pygame.draw.circle(screen, RED, [x,y], width, 0)
    # pygame.display.update()

    # font = pygame.font.SysFont('Calibri', 25, True, False)
    # text = font.render("Apollo", True, BLACK)
    # screen.blit(text, [x-5, y])


# coin
coin = pygame.image.load('coin.png')
speedy = 3
lx, ly = [], []
# random position
for i in range(0, 4):
    tx = 2 * random.randint(0, (screen_width - 48) / 2)
    ty = (i - 1) * 150
    lx.append(tx)
    ly.append(ty)
"""
# arrow 
speedx = 0
brick = pygame.transform.scale(pygame.image.load("arrow.jpg"), (91, 53))
bx, by = [], []
# random position
for i in range (0, 2):
  x = random.randint(0, (screen_width - 48) / 2)
  y = (i - 1) * 300
  bx.append(x)
  by.append(y)
 
class Brick:
    def __init__(self):
        self.brick_img = pygame.transform.scale(pygame.image.load("brick.png"), (91, 53))
        self.brick_img_rect = self.brick_img.get_rect()
        self.brick_img_rect.bottom = screen_height

    def update(self):
        screen.blit(self.brick_img, self.brick_img_rect)
"""

# Game loop
font = pygame.font.SysFont("calibri", 30, True)
player = Player(100, 333, 64, 64)

score = 0
level = 1
hp = 4
cannon = Cannon(True)
cannon2 = Cannon(False)
add_new_bomb_counter = 0
bombs_list = []
player.health = hp
bricks = []
levels = "B B B B B B "

'''
x = 0
for row in levels:
    Brick((x, screen_height-53))
    x += random.randrange(100, 500)
'''

alive = True
done = False
while not done:
    hp = 3
    player.health = 10
    if hp > 0:
        screen.blit(bg, (0, 0))
        # pygame.draw.rect(screen, BLACK, brick.rect)
        cannon.update()
        add_new_bomb_counter += 1
        coins_velocity = 5

        if score < 0:
            game_over()

        elif score < 50:
            speedy = 2
            # speedx = 0
            level = 1
            Brick((-100, screen_height - 100), 1000)

           # Brick((200, screen_height - 400))
           # Brick((350, screen_height - 200))
           # bricks.append(Brick)

        elif 100 > score >= 50:
            speedy = 3
            # speedx = 2
            level = 2
            x = 0
            Brick((50, screen_height - 100), 325)
            Brick((425, screen_height - 100), 325)
            if player.y >= 333:
                if 0 < player.x < 50 or 325 < player.x < 425 or 700 < player.x < screen_width:
                    player.y += 8
                    if player.y > screen_height-100:
                        player.vel = 0
                # alive = False
            # if player.y > 353:
            #    alive = True
            if player.y > screen_height or not alive:
                game_over()

        elif score >= 100:
            speedy = 4
            # speedx = 3
            level = 3
            Brick((50, screen_height-100), 200)
            Brick((300, screen_height-100), 200)
            Brick((550, screen_height-100), 200)
            if player.y >= 333:
                if 0 < player.x < 50 or 250 < player.x < 300 or 500 < player.x < 550 \
                        or 750 < player.x < screen.width:
                    player.y += 8
                # alive = False
            # if player.y > 353:
            #    alive = True
            if player.y > screen_height or not alive:
                game_over()



        # coins
        for i in range(len(lx)):
            screen.blit(coin, (lx[i], ly[i] - 500))
            ly[i] += speedy
            if ly[i] > 500 + screen_height:
                ly[i] = (random.randint(0,4)-1) * random.randint(140,160)
                lx[i] = 2 * random.randint(0, (screen_width - 48) / 2)
                score -= 5

            # collision
            if player.x < lx[i] + 24 < player.x + 64 and player.y - 10 <= ly[i]-500 <= player.y + 60:
                ly[i] = (random.randint(0,4)-1) * random.randint(40,120)
                lx[i] = 2 * random.randint(0, (screen_width - 48) / 2)
                score += 10

       # for brick in bricks:
            #if brick.brick_img_rect.colliderect(player.hitbox):
            #print("hit")

        # add new bomb
        if add_new_bomb_counter == ADD_NEW_BOMB_RATE:
            add_new_bomb_counter = 0
            new_bomb = Bombs(cannon)
            bombs_list.append(new_bomb)

        # remove bomb if outside the screen
        for b in bombs_list:
            if b.bombs_img_rect.left <= 0:
                bombs_list.remove(b)
            b.update()

        # bomb collision
        for b in bombs_list:
            if b.bombs_img_rect.colliderect(player.hitbox):
                game_over()

        # platform collision

        # for brick in bricks:
        #    screen.blit(brick.brick_img, brick.brick_img_rect)
        # if b.bombs_img_rect.colliderect(player.x):
        # hp -= 1

        # key control
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == keys:
                done = False

        if keys[pygame.K_LEFT] and player.x >= player.vel:
            player.x -= player.vel
            player.left = True
            player.right = False

        elif keys[pygame.K_RIGHT] and player.x < screen_width - player.width:
            player.x += player.vel
            player.right = True
            player.left = False
        else:
            player.left = False
            player.right = False
            player.walkCount = 0

        if not player.isJump:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                player.isJump = True
                player.right = False
                player.left = False
                player.walkCount = 0

        else:
            if player.jumpCount >= -10:
                neg = 1
                if player.jumpCount < 0:
                    neg = -1
                player.y -= player.jumpCount ** 2 * 0.4 * neg
                player.jumpCount -= 1
            else:
                player.isJump = False
                player.jumpCount = 10

        redrawGameWindow()

        pygame.display.flip()

        clock.tick(FPS)
