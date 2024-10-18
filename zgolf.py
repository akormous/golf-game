import pygame
from ball import Ball
from platform_box import PlatformBox
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create a sprite group and instances
    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()

    # Create a green platform
    platform = PlatformBox(x=0, y=500, width=SCREEN_WIDTH, height=20)
    platforms.add(platform)
    all_sprites.add(platform)

    # Create a Ball instance
    ball = Ball(x=400, y=300, radius=20, color=(255, 0, 0))
    all_sprites.add(ball)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        all_sprites.update(platforms)

        screen.fill((255, 255, 255))  # Clear the screen
        all_sprites.draw(screen)  # Draw all sprites
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()