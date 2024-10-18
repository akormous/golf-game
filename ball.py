import pygame
import random
from constants import GRAVITY, DAMP, FRICTION_COEFFICIENT, SCREEN_WIDTH


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))

        self.velocity = pygame.Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
        self.gravity = pygame.Vector2(0, GRAVITY)
        self.damping = DAMP
        self.friction = FRICTION_COEFFICIENT

    def update(self, platforms):
        # Apply gravity to the velocity
        self.velocity += self.gravity
        
        # Update the position of the ball
        self.rect.center += self.velocity
        
        # Check for collision with platforms
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity.y > 0:
                self.rect.bottom = platform.rect.top
                self.velocity.y *= -self.damping  # Reverse and dampen the velocity
                
                # Apply friction when touching the platform
                self.velocity.x *= self.friction
        
        # Check for collision with the walls
        if self.rect.left <= 0:
            self.rect.left = 0
            self.velocity.x *= -self.damping  # Reverse and dampen the velocity
        elif self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.velocity.x *= -self.damping  # Reverse and dampen the velocity

        # Stop the ball if velocity is very low
        if abs(self.velocity.x) < 0.1 and abs(self.velocity.y) < 0.1:
            self.velocity.x = 0
            self.velocity.y = 0

    # def draw(self, screen):
    #     pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    # def move(self):
    #     self.x += self.speed_x
    #     self.y += self.speed_y

    # def set_speed(self, speed: pygame.math.Vector2):
    #     self.speed_x = speed.x
    #     self.speed_y = speed.y

    # def set_speed_x(self, speed_x):
    #     self.speed_x = speed_x

    # def set_speed_y(self, speed_y):
    #     self.speed_y = speed_y

    # def get_speed_x(self):
    #     return self.speed_x

    # def get_speed_y(self):
    #     return self.speed_y

    # def get_pos(self):
    #     return pygame.Vector2(self.x, self.y)
