#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/2/7
# @Author : 郑煜辉
# @File : Peashooter

import pygame
from bullet import Buttet


class Peashooter(pygame.sprite.Sprite):
    def __init__(self):
        super(Peashooter, self).__init__()
        self.images = [pygame.image.load('images/plants/Peashooter/Peashooter_{:d}.png'.format(i)) for i in
                       range(13)]  # 实现动态效果
        self.rect = self.images[0].get_rect()
        self.rect.left = 200
        self.rect.top = 300
        self.zone = (0,0)
        self.blood = 50
        self.is_live = True

    def shot(self):
        return Buttet(self)
