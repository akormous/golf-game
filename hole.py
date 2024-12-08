# hole.py
import pygame

class Hole(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
