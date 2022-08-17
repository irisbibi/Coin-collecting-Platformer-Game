import random
import pygame
import sys

pygame.init()

# screen
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Don't get squashed!")

# instance variables
FPS = 20
ADD_NEW_BOMB_RATE = 10
coins_velocity = 5

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')


# color
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
font = pygame.font.SysFont('forte', 20)

# coins
"""
class Coins():
    def __init__(self, position):
        self.position = position
        self.coins_img = pygame.image.load("/Users/iriszhang/PycharmProjects/Pygame/coin.png")
        self.coins_img_rect = self.coins_img.get_rect()

    def update(self, coins_velocity):
        screen.blit(self.coins_img, self.position)
        self.position[1] += coins_velocity

    # image loading
"""
coins_img = pygame.image.load("/Users/iriszhang/PycharmProjects/Pygame/coin.png")
coins_img_rect = coins_img.get_rect()
# random position
coinx, coiny = [], []
for i in range(0, 4):
    newcoinx = random.randint(0, screen_width)
    newcoiny = (i - 1) * 150
    coinx.append(newcoinx)
    coiny.append(newcoiny)


# Class
class Cannon:
    cannon_velocity = 10

    def __init__(self):
        self.cannon_img = pygame.image.load("/Users/iriszhang/PycharmProjects/Pygame/cannon.png")
        self.cannon_img = pygame.transform.scale(self.cannon_img, (50, 50))
        self.cannon_img_rect = self.cannon_img.get_rect()
        self.cannon_img_rect.width -= 10
        self.cannon_img_rect.height -= 10
        self.cannon_img_rect.top = 0
        self.cannon_img_rect.right = screen_width / 2
        self.right = True
        self.left = False

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
    def __init__(self):
        self.bombs_img = pygame.image.load("/Users/iriszhang/PycharmProjects/Pygame/bomb.png")
        self.bombs_img = pygame.transform.scale(self.bombs_img, (30, 30))
        self.bombs_img_rect = self.bombs_img.get_rect()
        self.bombs_img_rect.left = cannon.cannon_img_rect.left
        self.bombs_img_rect.top = cannon.cannon_img_rect.bottom

    # move down the screen
    def update(self):
        screen.blit(self.bombs_img, self.bombs_img_rect)
        if self.bombs_img_rect.bottom > 0:
            self.bombs_img_rect.bottom += self.bombs_velocity


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

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

class projectle (object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 10*facing


# functions

# when game over
def game_over():
    game_over_img = pygame.image.load("/Users/iriszhang/PycharmProjects/Pygame/end.jpg")
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(game_over_img, game_over_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.flip()


# when pressed key, game start
def start_game():
    screen.fill(BLACK)
    start_img = pygame.image.load("/Users/iriszhang/PycharmProjects/Pygame/start.jpg")
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(start_img, start_img_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                hp = 3
                score = 0
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.flip()

player = player(50, 386, 64, 64)
# code for game loop
def game_loop():
    while True:
        global cannon
        cannon = Cannon()
        bombs = Bombs()
#        player = Player()
        add_new_bomb_counter = 0
        add_new_coin_counter = 0
        bombs_list = []
        coin_list = []
        coins_velocity = 5
        hp = 3
        score = 0


        # main game code
        while True:
            # background
            screen.fill(BLACK)
            # cannon movement
            cannon.update()
            add_new_bomb_counter += 1
            coins_velocity = 5
            score = 0
            text1 = font.render(str(score), True, WHITE)

            if 0 < hp < 4 and score >= 0:
                if score <= 50:
                    coins_velocity = 5
                if score > 100:
                    coins_velocity = 10
                if score > 150:
                    coins_velocity = 12
                if score > 175:
                    coins_velocity = 13

                # coin random location
                """
                y_position = 0
                x_position = random.randint(0, screen_width)
                coins_velocity = 5
                y_position += coins_velocity
                coin = Coins([x_position, y_position])
                coin_list.append(coin)
                for coin in coin_list:
                    coin.update(coins_velocity)
                """

                for i in range(len(coinx)):
                    screen.blit(text1, (570, 570))
                    screen.blit(coins_img, (coinx[i], coiny[i] - screen_height))
                    coiny[i] += coins_velocity
                    if coiny[i] > 600 + 610:
                        coiny[i] = 600
                        coinx[i] = random.randint(0, 540)
                        text1 = font.render(str(score), True, WHITE)

                        # coin collision
#                    if coins_img_rect.colliderect(player.player_img_rect):
                #        score += 10
               #         text1 = font.render(str(score), True, WHITE)

            # add new comb
            if add_new_bomb_counter == ADD_NEW_BOMB_RATE:
                add_new_bomb_counter = 0
                new_bomb = Bombs()
                bombs_list.append(new_bomb)

            # remove bomb if outside the screen
            for b in bombs_list:
                if b.bombs_img_rect.left <= 0:
                    bombs_list.remove(b)
                b.update()

            # bomb collision
          #  for b in bombs_list:
                # When player hit the bomb, terminate the game
#                if b.bombs_img_rect.colliderect(player.player_img_rect):
                 #   game_over()

            # key control
            keys = pygame.key.get_pressed()

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
                if keys[pygame.K_SPACE]:
                    player.isJump = True
                    player.right = False
                    player.left = False
                    player.walkCount = 0
            else:
                if player.jumpCount >= -10:
                    neg = 1
                    if player.jumpCount < 0:
                        neg = -1
                    player.y -= player.jumpCount ** 2 * 0.5 * neg
                    player.jumpCount -= 1
                else:
                    player.isJump = False
                    player.jumpCount = 10


            pygame.display.flip()
            clock.tick(FPS)


start_game()
