#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/2/7
# @Author : 郑煜辉
# @File : Peashooter

import pygame


class WallNut:
    def __init__(self):
        self.images = [pygame.image.load('images/plants/WallNut/WallNut_{:d}.png'.format(i)) for i in
                       range(16)]  # 实现动态效果
        self.rect = self.images[0].get_rect()
        self.rect.left = 200
        self.rect.top = 100
