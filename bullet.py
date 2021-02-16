#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/2/7
# @Author : 郑煜辉
# @File : Peashooter

import pygame


class Buttet(pygame.sprite.Sprite):
    def __init__(self,plant):
        super(Buttet,self).__init__()
        self.images = pygame.image.load('images/bullets/peaBullet.png').convert_alpha()
        self.rect = self.images.get_rect()
        self.rect.left = plant.zone[0]+35
        self.rect.top = plant.zone[1]
        self.speed = 15
        self.status = True
        self.attact = 1

    def move(self):
        if self.rect.left<1200:
            self.rect.left+=self.speed
        else:
            self.status = False




    def hit(self,enemyList):
        for enemy in enemyList:
            if pygame.sprite.collide_circle_ratio(0.5)(enemy,self):
                enemy.blood-=self.attact
                if enemy.blood == 0:
                    enemy.is_live = False
                self.status = False
