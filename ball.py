import pygame
import random
import math
from constants import BallConstants, Physics, Screen, Colors

# Ball properties
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [0, 0]
        self.is_aiming = False  # Track if aiming mode is active
        self.aim_start = None  # Store the aiming start position
        self.radius = radius

    def update(self, platforms):
        if not self.is_aiming:  # Only apply physics when not aiming
            # Apply gravity
            self.velocity[1] += Physics.GRAVITY

            # Apply damping
            self.velocity[0] *= Physics.DAMP
            self.velocity[1] *= Physics.DAMP

            # Move the ball
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

            # Check collisions with platforms
            for platform in platforms:
                if self.rect.colliderect(platform.rect):
                    if self.velocity[1] > 0 and self.rect.bottom >= platform.rect.top:
                        # Collision from above
                        self.rect.bottom = platform.rect.top
                        self.velocity[1] = -self.velocity[1] * Physics.FRICTION_COEFFICIENT
                    elif self.velocity[1] < 0 and self.rect.top <= platform.rect.bottom:
                        # Collision from below
                        self.rect.top = platform.rect.bottom
                        self.velocity[1] = -self.velocity[1] * Physics.FRICTION_COEFFICIENT
                    elif self.velocity[0] > 0 and self.rect.right >= platform.rect.left:
                        # Collision from the left
                        self.rect.right = platform.rect.left
                        self.velocity[0] = -self.velocity[0] * Physics.FRICTION_COEFFICIENT
                    elif self.velocity[0] < 0 and self.rect.left <= platform.rect.right:
                        # Collision from the right
                        self.rect.left = platform.rect.right
                        self.velocity[0] = -self.velocity[0] * Physics.FRICTION_COEFFICIENT

            # Prevent ball from leaving the screen
            if self.rect.left <= 0 or self.rect.right >= Screen.SCREEN_WIDTH:
                self.velocity[0] = -self.velocity[0] * Physics.FRICTION_COEFFICIENT
                if self.rect.left <= 0:
                    self.rect.left = 0
                else:
                    self.rect.right = Screen.SCREEN_WIDTH

            if self.rect.top <= 0:
                self.velocity[1] = -self.velocity[1] * Physics.FRICTION_COEFFICIENT
                self.rect.top = 0
            elif self.rect.bottom >= Screen.SCREEN_HEIGHT:
                self.velocity[1] = -self.velocity[1] * Physics.FRICTION_COEFFICIENT
                self.rect.bottom = Screen.SCREEN_HEIGHT

    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not self.is_aiming:
                # Enter aiming mode
                self.is_aiming = True
                self.aim_start = self.rect.center
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.is_aiming:
                self.is_aiming = False
                aim_end = pygame.mouse.get_pos()
                self.shoot(aim_end)

    def shoot(self, aim_end):
        if self.aim_start:
            # Calculate velocity based on the aiming distance (opposite direction)
            dx = self.aim_start[0] - aim_end[0]  # Invert direction for movement
            dy = self.aim_start[1] - aim_end[1]  # Invert direction for movement
            self.velocity = [dx * 0.1, dy * 0.1]  # Scale the shot power (note direction is reversed)

    def draw_aiming_indicator(self, screen):
        if self.is_aiming and self.aim_start:
            mouse_pos = pygame.mouse.get_pos()
            # Calculate the distance and angle (draw line to mouse position)
            dx = mouse_pos[0] - self.aim_start[0]  # Direction of power line (from ball to mouse)
            dy = mouse_pos[1] - self.aim_start[1]
            distance = math.sqrt(dx ** 2 + dy ** 2)
            angle = math.atan2(dy, dx)

            # Draw the dotted line in the direction of the mouse (where the ball will go)
            max_dots = int(distance // 10)
            for i in range(max_dots):
                t = i / max_dots
                dot_x = self.aim_start[0] + dx * t
                dot_y = self.aim_start[1] + dy * t
                
                pygame.draw.circle(screen, Colors.BLACK, (int(dot_x), int(dot_y)), 5)
