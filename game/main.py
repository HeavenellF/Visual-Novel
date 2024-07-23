import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Visual Novel")

# Main game loop
def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((255, 255, 255))  # Fill the screen with white
        pygame.display.flip()         # Update the display
        clock.tick(60)                # Cap the frame rate to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()