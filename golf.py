from ball import Ball
from constants import COORD_X, COORD_Y, GRASS, RADIUS, RED, SCREEN_LENGTH, SCREEN_WIDTH, SKY, SPEED_X, SPEED_Y, WHITE, YELLOW
from game import Game
import pygame
from utils import draw_dotted_line

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))

terrain = pygame.Rect(0, 720, SCREEN_WIDTH, 360)
ball = Ball(COORD_X, COORD_Y, RADIUS, WHITE, SPEED_X, SPEED_Y)

game = Game(terrain)
dragging = False
initial_mouse_pos = pygame.math.Vector2(0,0)

# Game loop
running = True
while running:
    screen.fill(SKY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the click is on the ball
            mouse_pos = pygame.math.Vector2(event.pos)
            if (mouse_pos - game.ball.get_pos()).length() <= game.ball.radius:
                dragging = True
                initial_mouse_pos = mouse_pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                # Calculate the velocity vector
                final_mouse_pos = pygame.math.Vector2(event.pos)
                drag_vector = initial_mouse_pos - final_mouse_pos
                ball_velocity = drag_vector * 0.1 # Scale down the speed
                game.ball.set_speed( ball_velocity )
                dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            # Update the position of the ball (optional, for a drag effect)
            pass
    


    game.ball.move()
    game.simulate_physics()

    pygame.draw.rect(screen, GRASS, game.terrain)
    game.ball.draw(screen)

    if dragging:
        current_mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        drag_vector = initial_mouse_pos - current_mouse_pos
        if drag_vector.length() > 0:  # Check if the drag vector is not zero
            arrow_end_pos = game.ball.get_pos() + drag_vector
            draw_dotted_line(screen, game.ball.get_pos(), arrow_end_pos, RED)

    pygame.display.flip()
    clock.tick(60)
