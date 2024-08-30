from constants import DAMP, GRAVITY, SCREEN_LENGTH, SCREEN_WIDTH
import pygame
from utils import sign

class Ball:
    def __init__(self, x, y, radius, color, speed_x=0, speed_y=0):
        # center coordinates
        self.x = x
        self.y = y
        # radius
        self.radius = radius
        self.color = color
        self.speed_x = speed_x # speed in x axis
        self.speed_y = speed_y # speed in y axis

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def set_speed_x(self, speed_x):
        self.speed_x = speed_x

    def set_speed_y(self, speed_y):
        self.speed_y = speed_y

    # reduces the speed by a factor of DAMP
    def damp(self, speed):
        return sign(speed) * (abs(speed) - DAMP)


    def invert_speed_y(self):
        if abs(self.speed_y) < DAMP:
            self.speed_y = 0
        else:
            self.speed_y = self.damp(self.speed_y)
            self.speed_y = -self.speed_y

    def invert_speed_x(self):
        if abs(self.speed_x) < DAMP:
            self.speed_x = 0
        else:
            self.speed_x = self.damp(self.speed_x)
            self.speed_x = -self.speed_x


    def simulate_gravity_x(self):
        if self.speed_x != 0:
            self.speed_x = sign(self.speed_x) * (abs(self.speed_x) - GRAVITY)

    def simulate_gravity_y(self):
        self.speed_y += GRAVITY

    def is_out_of_bounds(self):
        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH or self.y - self.radius < 0 or self.y + self.radius > SCREEN_LENGTH:
            return True
        return False
    
    def is_out_of_bounds_x(self):
        if self.x - self.radius < 0:
            self.x = self.radius
            self.invert_speed_x()
            return True
        elif self.x + self.radius > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.radius
            self.invert_speed_x()
            return True
        return False


    def is_colliding(self, terrain):
        if self.y + self.radius >= terrain.top:
            self.y = terrain.top - self.radius
            return True
        return False
    


