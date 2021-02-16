#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/2/7
# @Author : 郑煜辉
# @File : main

import pygame
import sys
from Peashooter import Peashooter
from Sunflower import SunFlower
from Wallnut import WallNut
from sun import Sun
from zone import Zone
from zombie import Zombie

pygame.init()

# 初始化音乐模块
pygame.mixer.init()
# 加载音乐
pygame.mixer.music.load("pvz.mp3")

screen_size = (1200, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('pvz')  # 窗口名
# 背景图地址
bg_path = 'images/Background.jpg'
backgroud = pygame.image.load(bg_path).convert()
# 卡槽
sg_path = 'images/cardSlot.png'
card_slot = pygame.image.load(sg_path).convert()
# 暂停
pause_draw = pygame.image.load('images/pause.png').convert_alpha()
# 结束
final_draw = pygame.image.load('images/final.png').convert_alpha()
# 卡片
card = pygame.image.load('images/cards/card_peashooter.png').convert()
card_1 = pygame.image.load('images/cards/card_sunflower.png').convert()
card_2 = pygame.image.load('images/cards/card_wallnut.png').convert()
card_rect = card.get_rect()
card_1_rect = card_1.get_rect()
card_2_rect = card_2.get_rect()
scale = 0.8
card = pygame.transform.scale(card, (int(card_rect.width * scale), int(card_rect.height * scale)))
card_1 = pygame.transform.scale(card_1, (int(card_1_rect.width * scale), int(card_1_rect.height * scale)))
card_2 = pygame.transform.scale(card_2, (int(card_2_rect.width * scale), int(card_2_rect.height * scale)))
# 阳光数
sunnum = '700'  # 初始阳光数
font = pygame.font.SysFont('arial', 20)
fontImg = font.render(sunnum, True, (0, 0, 0))


def main():
    global sunnum, font, fontImg
    # peashooter = Peashooter()
    clickimage = []
    # sunflower = SunFlower()
    wallnut = WallNut()
    p1 = []
    peaList = []
    sunFlowerList = []

    sunList = []
    zombieList = []
    zombie = Zombie()
    zombieList.append(zombie)

    enemy_zombie_list = []

    flower_product_list = []

    # FPS
    block = pygame.time.Clock()

    index = 0
    # 是否点击卡片
    is_pick = False
    # 区域种植判断
    is_plant = False
    # 太阳下落时间
    SUN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SUN_EVENT, 3000)  # 3秒出现一个

    # 太阳花产能
    FLOWER_PRODUCT_SUM_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(FLOWER_PRODUCT_SUM_EVENT, 5000)

    #
    ZOMBIE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ZOMBIE_EVENT, 5000)

    z = Zone()
    bulletList = []
    PAUSE = False
    FINAL = 0

    while 1:

        pygame.mixer.music.play()  # 播放音乐
        block.tick(25)  # FPS为25

        # 鼠标点击
        press = pygame.mouse.get_pressed()
        # 鼠标坐标
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == SUN_EVENT:
                sun = Sun()
                sunList.append(sun)
            # 太阳花产能
            if event.type == FLOWER_PRODUCT_SUM_EVENT:
                for flower in sunFlowerList:
                    if not flower.isProductSum:
                        sun = Sun()
                        sun.rect.left = flower.rect.left
                        sun.rect.top = flower.rect.top
                        sun.belong = flower
                        flower_product_list.append(sun)
                        flower.isProductSum = True  # 无法生产

            if event.type == ZOMBIE_EVENT:
                zombie = Zombie()
                zombieList.append(zombie)

            # 暂停，点击ESC
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    PAUSE = not PAUSE

            if event.type == pygame.MOUSEMOTION:
                if 537 <= x <= 749 and 378 <= y <= 481:
                    if press[0]:
                        PAUSE = not PAUSE
                if not is_pick:
                    if press[0]:
                        if 330 <= x <= 330 + card.get_rect().width and 7 <= y <= 7 + card.get_rect().height:
                            peashooter = Peashooter()
                            clickimage.append(peashooter)
                            pick_type = 'pea'
                            is_pick = True
                        if 380 <= x <= 380 + card_1.get_rect().width and 7 <= y <= 7 + card_1.get_rect().height:
                            sunflower = SunFlower()
                            clickimage.append(sunflower)
                            pick_type = 'flower'
                            is_pick = True

                else:
                    if z.is_plant_zone(x, y):
                        if z.getIndex(x, y) and not is_plant:
                            if pick_type == 'pea':
                                p = Peashooter()
                                a, b = z.getIndex(x, y)
                                p.zone = z.getGridPos(a, b)
                                if not z.plantInfo[b][a]:
                                    p1.append(p)
                                    is_plant = True
                                    if press[0]:
                                        peaList.append(p)
                                        enemy_zombie_list.append(p)
                                        # bullet = p.shot()
                                        # bulletList.append(bullet)
                                        clickimage.clear()
                                        p1.clear()
                                        is_pick = False
                                        z.plantInfo[b][a] = 1
                                        sunnum = str(int(sunnum) - 100)
                                        fontImg = font.render(sunnum, True, (0, 0, 0))

                                        # print(z.plantInfo[a][b])
                            elif pick_type == 'flower':
                                f = SunFlower()
                                a, b = z.getIndex(x, y)
                                f.zone = z.getGridPos(a, b)
                                if not z.plantInfo[b][a]:
                                    p1.append(f)
                                    is_plant = True
                                    if press[0]:
                                        sunFlowerList.append(f)
                                        enemy_zombie_list.append(f)
                                        clickimage.clear()
                                        p1.clear()
                                        is_pick = False
                                        z.plantInfo[b][a] = 1
                                        sunnum = str(int(sunnum) - 100)
                                        fontImg = font.render(sunnum, True, (0, 0, 0))
                        else:
                            p1.clear()
                            is_plant = False

                    if press[2]:
                        is_pick = False
                        clickimage.clear()
                        p1.clear()
                        is_plant = False

                        # if 330 <= x <= 405 and 180 <= y <= 274:

                    # else:
                    #     p1.clear()

                for sun in sunList:
                    if sun.rect.collidepoint((x, y)):
                        if press[0]:
                            # 点击太阳消失
                            sunList.remove(sun)
                            # 收集加分
                            # global sunnum, font, fontImg
                            sunnum = str(int(sunnum) + 25)
                            fontImg = font.render(sunnum, True, (0, 0, 0))

                for sun in flower_product_list:
                    if sun.rect.collidepoint((x, y)):
                        if press[0]:
                            # 点击太阳消失
                            flower_product_list.remove(sun)
                            # 收集加分
                            sunnum = str(int(sunnum) + 25)
                            fontImg = font.render(sunnum, True, (0, 0, 0))
                            # 收集后可继续生产
                            sun.belong.isProductSum = False

        # 打印图片
        if int(zombie.rect.left) < 200:
            FINAL += 1
            PAUSE = True
        if not PAUSE:
            screen.blit(backgroud, (0, 0))
            screen.blit(card_slot, (250, 0))
            screen.blit(card, (330, 7))
            screen.blit(card_1, (380, 7))
            screen.blit(card_2, (430, 6))
            screen.blit(fontImg, (275, 60))

            if index > 13:
                index = 0
            # screen.blit(peashooter.images[index % 13], peashooter.rect)
            # screen.blit(sunflower.images[index % 18], sunflower.rect)
            # screen.blit(wallnut.images[index % 16], wallnut.rect)

            for image in clickimage:
                screen.blit(image.images[0], (x, y))
            for p in p1:
                screen.blit(p.images[0], p.zone)
            # 豌豆射手
            for pea in peaList:
                if pea.is_live:
                    if index % 99 == 1:
                        bullet = pea.shot()
                        bulletList.append(bullet)
                    screen.blit(pea.images[index % 13], pea.zone)
                else:
                    peaList.remove(pea)
                    enemy_zombie_list.remove(pea)
            # 太阳花
            for sunFlower in sunFlowerList:
                if sunFlower.is_live:
                    screen.blit(sunFlower.images[index % 18], sunFlower.zone)
                else:
                    sunFlowerList.remove(sunFlower)
                    enemy_zombie_list.remove(sunFlower)
            # 阳光
            for sun in sunList:
                screen.blit(sun.images[index % 22], sun.rect)
                sun.down()

            # 产能
            for sun in flower_product_list:
                screen.blit(sun.images[index % 22], sun.rect)

            for bullet in bulletList:
                if bullet.status:
                    screen.blit(bullet.images, bullet.rect)
                    bullet.move()
                    bullet.hit(zombieList)
                else:
                    bulletList.remove(bullet)

            for zombie in zombieList:
                if zombie.is_live:
                    zombie.changimage()
                    screen.blit(zombie.images[index % 20], zombie.rect)
                    zombie.move()
                    zombie.attack(enemy_zombie_list)
                else:
                    zombieList.remove(zombie)

            pygame.display.update()

            index += 1
        else:
            if FINAL > 0:
                screen.blit(final_draw, (350, 70))
            else:
                screen.blit(pause_draw, (450, 100))

        pygame.display.update()


if __name__ == '__main__':
    main()
