from config import *
import pygame

class Bat:
    def __init__(self):
        #координаты ракетки
        self.x = BAT_OFFSET
        self.y = 980
        #скорость ракетки
        self.speed_x = 0

    def update(self):
        keys = pygame.key.get_pressed()
        #если нажата
        if keys[pygame.K_RIGHT]:
            self.speed_x = 10
        #если нажата
        if keys[pygame.K_LEFT]:
            self.speed_x = -10
        self.x += self.speed_x
        self.speed_x = 0
        if self.x <= 0:
            self.x = 0
        elif self.x >= SCREEN_WIDTH - BAT_WIDTH:
            self.x = SCREEN_WIDTH - BAT_WIDTH
