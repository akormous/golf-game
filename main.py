# main.py
import pygame
import sys
from ball import Ball
from platform_box import PlatformBox
from hole import Hole
from level import Level
from constants import Screen, Colors, BallConstants

# Game setup
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
# Load the background
background = pygame.image.load('./images/sky.jpg')
# Scale the image to fit the screen
background = pygame.transform.scale(background, (Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))

screen = pygame.display.set_mode((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT))
pygame.display.set_caption("Golf Game")

# Create level components
platforms = [
    PlatformBox(0, Screen.SCREEN_HEIGHT - 60, Screen.SCREEN_WIDTH, 60)
]
hole = Hole(700, 550, 30, Colors.YELLOW)

# Create level
level = Level(platforms, hole)

# Create ball
ball = Ball(BallConstants.COORD_X // 2, BallConstants.COORD_Y // 2, BallConstants.RADIUS, Colors.WHITE)

# Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ball.handle_mouse_event(event)

    # Update ball and level
    ball_reached_hole = ball.update(level.platforms)
    level.update()

    # Draw everything
    # screen.fill(Colors.WHITE)
    screen.blit(background, (0, 0))
    level.draw(screen)
    all_sprites.draw(screen)
    ball.draw_aiming_indicator(screen)

    if ball_reached_hole:
        print("Level Complete!")
        running = False  # End the game for now (you can load the next level here)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
