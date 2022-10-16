import pygame
import random
from pygame.sprite import *
from pygame.locals import *


class MovingBall(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface((30, 30))
        self.color = color

        pygame.draw.circle(self.image, self.color, (15, 15), 15, 0)

        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, 600)
        self.rect.centery = random.randrange(0, 600)
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

screen = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ball1 = MovingBall(RED)
ball2 = MovingBall(GREEN)
ball3 = MovingBall(BLUE)

ball_list = pygame.sprite.Group()
ball_list.add(ball1)
ball_list.add(ball2)
ball_list.add(ball3)

isEnd = False
while not isEnd:
    for event in pygame.event.get():
        if event.type == QUIT:
            isEnd = True

    if collide_rect(ball1, ball2):
        ball1.directionx *= -1
        ball1.directiony *= -1
        ball2.directionx *= -1
        ball2.directiony *= -1

    if collide_rect(ball1, ball3):
        ball1.directionx *= -1
        ball1.directiony *= -1
        ball3.directionx *= -1
        ball3.directiony *= -1

    if collide_rect(ball3, ball2):
        ball3.directionx *= -1
        ball3.directiony *= -1
        ball2.directionx *= -1
        ball2.directiony *= -1

    ball_list.update()

    screen.fill((0, 0, 0))

    ball_list.draw(screen)

    pygame.display.update()

    clock.tick(30)

pygame.quit()
