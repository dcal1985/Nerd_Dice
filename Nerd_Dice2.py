# import libraries
import pygame
import random

# set screen dimensions and refresh rate
WIDTH = 400
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# initialize pygame and create window
pygame.init()
pygame.font.init()


class Total:

    def __init__(self):

        self.list = []


# total for rolls
def draw_total(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# create button class
class Button:

    def __init__(self, image, x, y):

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (125, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw_button(self):
        screen.blit(self.image, self.rect)

    def update_totals(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                d4.count = 0
                d6.count = 0
                d8.count = 0
                d10.count = 0
                d12.count = 0
                d20.count = 0
                rolled.list = []
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


# create dice class
class Dice:

    def __init__(self, limit, image, x, y):

        self.limit = limit
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.count = 0
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw_dice(self):
        screen.blit(self.image, self.rect)
        cnt = font2.render(str(self.count).zfill(2), True, BLACK)
        screen.blit(cnt, (self.rect.left + 35, self.rect.bottom))
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                Dice.roll(self)
                self.count += 1
                print(self.count)
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

    # roll dice (add to roll total list & print instance)
    def roll(self):
        rolled.list.append(random.randrange(1, self.limit))


# game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nerd Dice")
background = pygame.image.load('img/table.png').convert()
background_rect = background.get_rect()
logo = pygame.image.load('img/logo.png').convert()
pygame.display.set_icon(logo)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Georgia", 65)
font2 = pygame.font.SysFont("Georgia", 25)

# create the dice
reset = Button('img/reset.png', 200, HEIGHT - 50)
d4 = Dice(5, 'img/d4.png', int(WIDTH / 6), int(HEIGHT / 3))
d6 = Dice(7, 'img/d6.png', int(WIDTH / 6) * 3, int(HEIGHT / 3))
d8 = Dice(9, 'img/d8.png', int(WIDTH / 6) * 5, int(HEIGHT / 3))
d10 = Dice(11, 'img/d10.png', int(WIDTH / 6), int(HEIGHT / 3) * 2)
d12 = Dice(13, 'img/d12.png', int(WIDTH / 6) * 3, int(HEIGHT / 3) * 2)
d20 = Dice(21, 'img/d20.png', int(WIDTH / 6) * 5, int(HEIGHT / 3) * 2)
rolled = Total()
# create the game loop

running = True
while running:
    # keep running at correct speed
    clock.tick(FPS)
    # process input
    for event in pygame.event.get():
        # check for escape
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rolled.list = []
                d4.count = 0
                d6.count = 0
                d8.count = 0
                d10.count = 0
                d12.count = 0
                d20.count = 0
            if event.key == pygame.K_a:
                Dice.roll(d4)
            if event.key == pygame.K_s:
                Dice.roll(d6)
            if event.key == pygame.K_d:
                Dice.roll(d8)
            if event.key == pygame.K_f:
                Dice.roll(d10)
            if event.key == pygame.K_g:
                Dice.roll(d12)
            if event.key == pygame.K_h:
                Dice.roll(d20)

    # draw/render

    screen.fill(WHITE)
    screen.blit(background, background_rect)
    if sum(rolled.list) > 999:
        roll_total = []
    else:
        draw_total(str(sum(rolled.list)).zfill(3), font, BLACK, int(WIDTH / 2.9), 20)
    d4.draw_dice()
    d6.draw_dice()
    d8.draw_dice()
    d10.draw_dice()
    d12.draw_dice()
    d20.draw_dice()
    reset.draw_button()
    reset.update_totals()

    # *after* drawing everything, flip display (double buffering)
    pygame.display.flip()

pygame.quit()

# test