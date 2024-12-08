import pygame
from constants import Screen

class PlatformBox(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, is_moving=False, speed=0):
        super().__init__()
        self.image = pygame.image.load('./images/ground_tile.png')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_moving = is_moving
        self.speed = speed
        self.initial_x = x  # For moving platforms

    def update(self):
        if self.is_moving:
            self.rect.x += self.speed
            if self.rect.left <= 0 or self.rect.right >= Screen.SCREEN_WIDTH:
                self.speed = -self.speed  # Reverse direction at edges
