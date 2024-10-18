from constants import GRAVITY, MAX_LAUNCH_POWER
import pygame
import math


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255), (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = radius
        self.velocity_y = 0
        self.velocity_x = 0
        self.dragging = False
        self.start_drag_pos = None
        self.bounce_damping = 0.8  # Damping factor for bounce
        self.is_launched = False  # To track if the ball is moving

    def apply_gravity(self):
        if not self.dragging:
            self.velocity_y += GRAVITY

    def update(self, platforms, WIDTH, HEIGHT):
        if not self.dragging and self.is_launched:
            self.apply_gravity()
            self.rect.y += self.velocity_y
            self.rect.x += self.velocity_x
            self.handle_bounds(WIDTH, HEIGHT)
            self.handle_collision_with_platforms(platforms)

    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and not self.is_launched:
                self.dragging = True
                self.start_drag_pos = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP and self.dragging:
            self.dragging = False
            self.is_launched = True
            end_drag_pos = event.pos
            self.launch_ball(end_drag_pos)
        
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            # Ball stays in place during dragging; just update the trajectory
            pass

    def launch_ball(self, end_drag_pos):
        dx = self.start_drag_pos[0] - end_drag_pos[0]
        dy = self.start_drag_pos[1] - end_drag_pos[1]

        # Calculate distance dragged
        distance = math.sqrt(dx**2 + dy**2)

        # Normalize drag direction and apply power
        angle = math.atan2(dy, dx)
        power = min(distance * 0.1, MAX_LAUNCH_POWER)  # Limit max power

        # Calculate velocity components
        self.velocity_x = math.cos(angle) * power
        self.velocity_y = math.sin(angle) * power

    def handle_collision_with_platforms(self, platforms):
        if pygame.sprite.spritecollide(self, platforms, False):
            if self.velocity_y > 0:
                self.velocity_y = -self.velocity_y * self.bounce_damping
                platform = pygame.sprite.spritecollide(self, platforms, False)[0]
                self.rect.bottom = platform.rect.top

    def handle_bounds(self, WIDTH, HEIGHT):
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.velocity_x = -self.velocity_x * self.bounce_damping
            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
        if self.rect.top > HEIGHT:
            self.reset_position(WIDTH // 2, HEIGHT // 2)

    def reset_position(self, x, y):
        self.rect.center = (x, y)
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_launched = False

    def draw_trajectory(self, screen):
        if not self.dragging:
            return
        
        # Calculate the initial velocity based on the drag
        dx = self.start_drag_pos[0] - self.rect.centerx
        dy = self.start_drag_pos[1] - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        angle = math.atan2(dy, dx)
        power = min(distance * 0.1, MAX_LAUNCH_POWER)
        
        # Calculate initial velocity
        init_vx = math.cos(angle) * power
        init_vy = math.sin(angle) * power
        
        # Predict trajectory by simulating the ball's movement
        x, y = self.rect.centerx, self.rect.centery
        vx, vy = init_vx, init_vy
        
        for i in range(1, 50):  # Predict next 50 frames
            # Update the predicted position
            x += vx
            y += vy
            vy += GRAVITY  # Gravity affects y-velocity

            # Draw a dot for each predicted position
            if i % 2 == 0:  # Draw every other step for dotted effect
                pygame.draw.circle(screen, (0, 255, 0), (int(x), int(y)), 5)
