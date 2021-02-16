#!/user/bin/python3
# -*- coding = utf-8 -*-
# @Time : 2021/2/8
# @Author : 郑煜辉
# @File : zone

class Zone:
    X_OFFSET_MAP = 250
    Y_OFFSET_MAP = 90

    X_GRID_SIZE = 80
    Y_GRID_SIZE = 90

    X_GRID_LEN = 9
    Y_GRID_LEN = 5

    def __init__(self):
        self.plantInfo = (
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        )

    def getIndex(self, x, y):
        x -= Zone.X_OFFSET_MAP
        y -= Zone.Y_OFFSET_MAP

        return x // Zone.X_GRID_SIZE, y // Zone.Y_GRID_SIZE

    def getGridPos(self, x, y):
        return x * Zone.X_GRID_SIZE + Zone.X_OFFSET_MAP, y * Zone.Y_GRID_SIZE + Zone.Y_OFFSET_MAP

    def is_card_slot(self, x, y, width, height):
        if 250 <= x <= 250 + width and 0 <= y <= height:
            return True
        else:
            return False

    def is_plant_zone(self, x, y):
        if Zone.X_OFFSET_MAP <= x <= Zone.X_OFFSET_MAP + Zone.X_GRID_SIZE * Zone.X_GRID_LEN and Zone.Y_OFFSET_MAP <= y <= Zone.Y_OFFSET_MAP + Zone.Y_GRID_SIZE * Zone.Y_GRID_LEN:
            return True
        else:
            return False
