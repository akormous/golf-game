# level.py
import pygame
from platform_box import PlatformBox
from hole import Hole

class Level:
    def __init__(self, platforms, hole):
        self.platforms = platforms
        self.hole = hole

    def update(self):
        for platform in self.platforms:
            platform.update()

    def draw(self, screen):
        for platform in self.platforms:
            screen.blit(platform.image, platform.rect)
        screen.blit(self.hole.image, self.hole.rect)
