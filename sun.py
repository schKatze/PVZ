#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/2/7
# @Author : 郑煜辉
# @File : Peashooter

import pygame
import random


class Sun(pygame.sprite.Sprite):
    def __init__(self):
        super(Sun,self).__init__()
        self.images = [pygame.image.load('images/Sun/Sun_{:d}.png'.format(i)) for i in
                       range(22)]  # 实现动态效果
        self.rect = self.images[0].get_rect()
        self.rect.left = random.choice([200, 300, 400])
        self.rect.top = 0
        self.speed = 5
        self.belong = None

    def down(self):
        self.rect.top += self.speed
