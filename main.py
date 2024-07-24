import pygame
import sys
from game.setting import Setting
from game.scene import Scene


# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Visual Novel")

# initialize Setting
setting = Setting()


# Main game loop
def main():

    running = True
    clock = pygame.time.Clock()
 
    scene = Scene(setting)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                setting.resize_display(1344, 756)
                scene = Scene(setting)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                setting.to_fullscreen()
                scene = Scene(setting)

        screen.fill((0, 0, 0))  # Fill the screen with black

        scene.draw(screen)


        pygame.display.flip()         # Update the display
        clock.tick(60)                # Cap the frame rate to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()