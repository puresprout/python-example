import random
import time

import pygame.image
from pygame.sprite import *
from pygame.locals import *


class MovingRect(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface((30, 30))
        self.color = color

        pygame.draw.rect(self.image, self.color, [0, 0, 30, 30])

        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(30, screen.get_width() - 30)
        self.rect.centery = random.randrange(30, screen.get_height() - 30)
        self.directionx = random.randrange(-10, 10)
        self.directiony = random.randrange(-10, 10)

    def bouncing(self):
        if self.rect.left <= 0 or self.rect.right >= screen.get_width():
            self.directionx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= screen.get_height():
            self.directiony *= -1

    def update(self):
        self.bouncing()
        self.rect.centerx += self.directionx
        self.rect.centery += self.directiony


pygame.init()

screen = pygame.display.set_mode((600, 480))

clock = pygame.time.Clock()

background = pygame.image.load("smearing_640.jpg")

ball_list = pygame.sprite.Group()

for i in range(1, 10):
    ball_list.add(MovingRect((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))

isEnd = False
while not isEnd:
    for event in pygame.event.get():
        if event.type == QUIT:
            isEnd = True

    start = time.time()

    ball_list.update()

    screen.blit(background, (0, 0))

    ball_list.draw(screen)

    pygame.display.update()

    end = time.time()

    print(end - start)

    clock.tick(30)

pygame.quit()
