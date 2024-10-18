import pygame
from platform import Platform

class Level:
    def __init__(self):
        self.platforms = pygame.sprite.Group()

    def setup_level(self, level_num):
        self.platforms.empty()  # Clear previous level platforms

        if level_num == 1:
            # Level 1 platforms
            self.platforms.add(Platform(0, 580, 800, 20))  # Ground
            self.platforms.add(Platform(200, 400, 200, 20))
            self.platforms.add(Platform(500, 300, 150, 20))

        elif level_num == 2:
            # Level 2 platforms
            self.platforms.add(Platform(0, 580, 800, 20))  # Ground
            self.platforms.add(Platform(300, 450, 100, 20))
            self.platforms.add(Platform(600, 350, 150, 20))
            self.platforms.add(Platform(100, 250, 200, 20))
        
        # Add more levels here...
