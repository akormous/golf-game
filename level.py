from constants import ALPHA, SCREEN_LENGTH
import pygame
import os

class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Level:
    def __init__(self):
        pass
    def ground(self, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        while i < len(gloc):
            ground = Platform(gloc[i], SCREEN_LENGTH - ty, tx, ty, 'ground_tile.png')
            ground_list.add(ground)
            i = i + 1
        return ground_list

    def platform(self, tx, ty):
        plat_list = pygame.sprite.Group()
        ploc = []
        i = 0
        ploc.append((200, SCREEN_LENGTH - ty - 128, 3))
        ploc.append((300, SCREEN_LENGTH - ty - 256, 3))
        ploc.append((500, SCREEN_LENGTH - ty - 128, 4))
        while i < len(ploc):
            j = 0
            while j <= ploc[i][2]:
                plat = Platform((ploc[i][0] + (j * tx)), ploc[i][1], tx, ty, 'ground_tile.png')
                plat_list.add(plat)
                j = j + 1
            i = i + 1
        return plat_list
