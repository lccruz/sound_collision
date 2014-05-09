# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
from Quadrado import *


pygame.init()

flags = DOUBLEBUF
screen = pygame.display.set_mode((600, 600),flags)
pygame.display.set_caption("Sounds")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0,0,0))

#cria os quadrados
quadrados_group = pygame.sprite.Group()
for i in range(0,10):
    quadrado = Quadrados()
    quadrados_group.add(quadrado)

clock = pygame.time.Clock()
count = 0
keepGoing = True
while keepGoing:
    clock.tick(30)
    background.fill((0,0,0))
    circulo = pygame.draw.circle(background, (255,255,255), (300, 300), 100)

    if count == 10:
        quadrado = Quadrados()
        quadrados_group.add(quadrado)
        count = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    quadrados_group.clear(screen, background)
    quadrados_group.update(circulo)
    quadrados_group.draw(background)

    screen.blit(background, (0, 0))

    pygame.display.flip()
    count += 1
