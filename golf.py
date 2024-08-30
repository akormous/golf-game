from ball import Ball
from constants import COORD_X, COORD_Y, GRASS, JUMP, RADIUS, SCREEN_LENGTH, SCREEN_WIDTH, SKY, SPEED_X, SPEED_Y, WHITE
import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))

terrain = pygame.Rect(0, 720, SCREEN_WIDTH, 360)
ball = Ball(COORD_X, COORD_Y, RADIUS, WHITE, SPEED_X, SPEED_Y)

running = True
# Game loop
while running:
    screen.fill(SKY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball.is_colliding(terrain):
        print("UP")
        ball.set_speed_y(-JUMP)
    elif keys[pygame.K_RIGHT]:
        print("RIGHT")
        ball.set_speed_x(JUMP)
    elif keys[pygame.K_LEFT]:
        print("LEFT")
        ball.set_speed_x(-JUMP)


    ball.move()
    if ball.is_out_of_bounds_x():
        print("STAY IN THE PLAY AREA!")

    if ball.is_colliding(terrain):
        ball.invert_speed_y()
    else:
        ball.simulate_gravity_y()

    ball.simulate_gravity_x()
    
    pygame.draw.rect(screen, GRASS, terrain)
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(60)
