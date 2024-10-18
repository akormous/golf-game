import pygame
from ball import Ball
from level import Level

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golf Game with Levels")

# Colors
WHITE = (255, 255, 255)

# Initialize level system and set up first level
level_manager = Level()
current_level = 1
level_manager.setup_level(current_level)

# Create ball sprite
ball = Ball(WIDTH // 2, HEIGHT // 2, 20)
ball_group = pygame.sprite.Group(ball)

# Main game loop
running = True
clock = pygame.time.Clock()

# In the main game loop

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse input for the ball
        ball.handle_mouse_event(event)

    # Update the ball's position and handle gravity and collisions
    ball_group.update(level_manager.platforms, WIDTH, HEIGHT)

    # Clear the screen
    screen.fill(WHITE)
    
    # Draw platforms and ball
    level_manager.platforms.draw(screen)
    ball_group.draw(screen)

    # Draw the trajectory when the ball is being dragged
    ball.draw_trajectory(screen)

    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)
pygame.quit()
