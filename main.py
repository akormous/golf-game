import pygame, sys

pygame.init()


# Size of the game screen
size = width, height = 1920, 1080
MOVE_SPEED = 1 
speed = [0,0]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

box_w, box_h = 100, 720
box_color = 255,0,0
box_color_2 = 255,255,255
box_rect = pygame.Rect(960, 100, box_w, box_h)


while True:
    # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP KEY PRESSED!")
                speed[1] = -MOVE_SPEED
            elif event.key == pygame.K_DOWN:
                print("DOWN KEY PRESSED!")
                speed[1] = MOVE_SPEED
            elif event.key  == pygame.K_LEFT:
                print("LEFT KEY PRESSED!")
                speed[0] = -MOVE_SPEED
            elif event.key == pygame.K_RIGHT:
                print("RIGHT KEY PRESSED!")
                speed[0] = MOVE_SPEED
            
    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = 0
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = 0

    if ballrect.colliderect(box_rect):
        print("Collsion detected!")
        speed[0] = 0
        speed[1] = 0
        box_color = box_color_2

    
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.draw.rect(screen, box_color, box_rect)
    pygame.display.flip()
