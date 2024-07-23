import pygame
import sys
from game.dialogbox import DialogueBox
from game.setting import Setting


# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Visual Novel")

# initialize Setting
setting = Setting()
screen_width, screen_height = setting.get_dimensions()


# Main game loop
def main():

    running = True
    clock = pygame.time.Clock()

    # Create an instance of DialogueBox
    dialogue_box = DialogueBox(50, 700, screen_width-100, screen_height-750, (100, 100, 100))
    dialogue_box.set_name("Character Name")
    dialogue_box.set_dialogue("This is a sample dialogue for testing the DialogueBox.")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((0, 0, 0))  # Fill the screen with white

        dialogue_box.draw(screen)


        pygame.display.flip()         # Update the display
        clock.tick(60)                # Cap the frame rate to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()