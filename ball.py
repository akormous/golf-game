import pygame

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

    def set_speed(self, speed: pygame.math.Vector2):
        self.speed_x = speed.x
        self.speed_y = speed.y

    def set_speed_x(self, speed_x):
        self.speed_x = speed_x

    def set_speed_y(self, speed_y):
        self.speed_y = speed_y

    def get_speed_x(self):
        return self.speed_x

    def get_speed_y(self):
        return self.speed_y

    def get_pos(self):
        return pygame.Vector2(self.x, self.y)
    


