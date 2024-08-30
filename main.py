import pygame, sys
import ball

pygame.init()

clock = pygame.time.Clock()

# Size of the game screen
size = width, height = 1920, 1080
MOVE_SPEED = 1 
speed = [0,1]
black = 0,0,0
sky = 90,204,219
night_sky = 35,81,87
screen = pygame.display.set_mode(size)

ball = ball.Ball(x=250, y=250, radius=20, color=(0, 0, 255), speed_x=2, speed_y=2)

ballrect = ball.get_rect()

ground_rect = pygame.Rect(0, 980, width, 100)
ground_color = 81, 214, 90

jump_height = 15
gravity = 1

while True:
    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("JUMP!")
            elif event.key == pygame.K_DOWN:
                print("DOWN KEY PRESSED!")
            elif event.key  == pygame.K_LEFT:
                print("LEFT KEY PRESSED!")
            elif event.key == pygame.K_RIGHT:
                print("RIGHT KEY PRESSED!")
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ballrect.bottom == 980:
        speed[1] = -jump_height
    elif keys[pygame.K_RIGHT]:
        speed[0] = jump_height


    ballrect = ballrect.move(speed)
    speed[1] += gravity
    if speed[0] != 0:
        speed[0] -= gravity
    
    if ballrect.bottom >= 980:
        ballrect.bottom = 980
        speed[1] = 0

    # if ball is out of bounds
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


       
    screen.fill(night_sky)
    screen.blit(ball, ballrect)
    pygame.draw.rect(screen, ground_color, ground_rect)
    pygame.display.flip()
    clock.tick(60)
