#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/2/7
# @Author : 郑煜辉
# @File : Peashooter

import pygame
import random


class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super(Zombie, self).__init__()
        self.images = [pygame.image.load('images/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha() for i in
                       range(22)]  # 实现动态效果
        self.rect = self.images[0].get_rect()
        self.rect.left = 1000
        self.rect.top = 25 + random.randrange(0,4)*125
        self.speed = 1
        self.blood = 25
        self.is_live = True
        self.stop = False
        # self.final = False
        self.kill = 1
        self.old = 0

    def move(self):
        if not self.stop:
            self.rect.left -= self.speed

    def changimage(self):
        if self.old ==0:
            self.images = [pygame.image.load('images/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha() for i in
                           range(22)]  # 实现动态效果
        elif self.old == 1:
            self.images = [pygame.image.load('images/ZombieAttack/ZombieAttack_{:d}.png'.format(i)).convert_alpha() for i in
                       range(20)]  # 实现动态效果

    def attack(self,enemyList):
        for enemy in enemyList:
            enemy.rect.left,enemy.rect.top = enemy.zone
            if pygame.sprite.collide_circle_ratio(0.5)(enemy,self):
                #print('hit')
                self.stop = True
                self.old =1
                enemy.blood-=self.kill
                if enemy.blood == 0:
                    enemy.is_live = False
                    self.stop = False
                    self.old=0

