import pygame
from pygame.sprite import *
from pygame.locals import *
import random


class Plane(Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.color = color

        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 350)

    def update(self, color):
        pass

    def moveToRight(self, speed):
        self.rect.x += speed

    def moveToLeft(self, speed):
        self.rect.x -= speed

    def moveToDown(self, speed):
        self.rect.y += speed


WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("sprite example")

clock = pygame.time.Clock()

airCraft = Plane(RED)

enemy1 = Plane((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
enemy1.rect.x = random.randint(0, 640)
enemy1.rect.y = 0

enemy2 = Plane((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
enemy2.rect.x = random.randint(0, 640)
enemy2.rect.y = -300

enemy3 = Plane((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
enemy3.rect.x = random.randint(0, 640)
enemy3.rect.y = -600

enemy4 = Plane((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
enemy4.rect.x = random.randint(0, 640)
enemy4.rect.y = -900

enemy_list = pygame.sprite.Group()
enemy_list.add(enemy1)
enemy_list.add(enemy2)
enemy_list.add(enemy3)
enemy_list.add(enemy4)

isEnd = False
while not isEnd:
    for event in pygame.event.get():
        if event.type == QUIT:
            isEnd = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        airCraft.moveToLeft(5)
    if keys[pygame.K_RIGHT]:
        airCraft.moveToRight(5)

    for enemy in enemy_list:
        enemy.moveToDown(5)
        if enemy.rect.y > screen.get_height():
            enemy.rect.x = random.randint(0, 640)
            enemy.rect.y = -100

        if pygame.sprite.collide_rect(airCraft, enemy):
            print("stop!")
            isEnd = True

    screen.fill(WHITE)
    screen.blit(airCraft.image, airCraft.rect.topleft)
    for enemy in enemy_list:
        screen.blit(enemy.image, enemy.rect.topleft)

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
