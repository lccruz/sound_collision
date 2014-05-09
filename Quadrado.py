# -*- coding: utf-8 -*-

import pygame
import random
from utils import get_color
from utils import get_pos

def dio():
    import os
    comando = 'mplayer audios/%s.mp3 &' % (random.randrange(1,16))
    os.system(comando)

class Quadrados(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cor = get_color()
        self.width,self.height = (40,40)
        self.x,self.y,self.dir = get_pos()
        self.imageMaster = pygame.Surface((self.width,self.height))
        self.imageMaster.fill(self.cor)
        self.imageMaster.set_colorkey((255,255,255))
        self.image = self.imageMaster
        pygame.draw.rect(self.image, self.cor, (self.x,self.y,self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = random.randrange(1,10)
        self.dx = 0 
        self.dy = 0 
        self.colide = False

    def update(self, circulo):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter

        self.calcVector()
        self.x += self.dx
        self.y += self.dy
        self.rect.centerx = self.x
        self.rect.centery = self.y

        #colisao
        if not self.colide:
            col_list = -1
            col = 0
            if self.dir == 315:
                col = self.rect.collidepoint(240,240)
            elif self.dir == 45:
                col = self.rect.collidepoint(360,240)
            elif self.dir == 135:
                col = self.rect.collidepoint(360,360)
            elif self.dir == 225:
                col = self.rect.collidepoint(240,360)
            else:
                col_list = self.rect.collidelist([circulo])

            if col or col_list != -1:
                self.colide = True
                self.speed = 0
                dio()
                self.kill()

    def calcVector(self):
        if self.dir == 0:
            self.dx = 0
            self.dy = 1
        elif self.dir == 45:
            self.dx = -1
            self.dy = 1
        elif self.dir == 90:
            self.dx = -1
            self.dy = 0
        elif self.dir == 135:
            self.dx = -1
            self.dy = -1
        elif self.dir == 180:
            self.dx = 0
            self.dy = -1
        elif self.dir == 225:
            self.dx = 1
            self.dy = -1
        elif self.dir == 270:
            self.dx = 1
            self.dy = 0
        elif self.dir == 315:
            self.dx = 1
            self.dy = 1
        else:
            print "erro"

        self.dx *= self.speed
        self.dy *= self.speed
