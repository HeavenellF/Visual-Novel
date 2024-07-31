import sys
import pygame
from game.setting import Setting
from game.scene import Scene


# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((1344, 756), pygame.RESIZABLE)
pygame.display.set_caption("Visual Novel")

# initialize Setting
setting = Setting()

game_state = "game"

# Main game loop
def main():

    running = True
    clock = pygame.time.Clock()
    scene = Scene(setting, "resources/story/storyTest.json")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                setting.resize_display(1344, 756)
                scene.init_dialogue_box()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                setting.to_fullscreen()
                scene.init_dialogue_box()
            
            if game_state == "game":
                input_in_game(event, scene)


        screen.fill((0, 0, 0))  # Fill the screen with black

        scene.draw(screen)


        pygame.display.flip()         # Update the display
        clock.tick(60)                # Cap the frame rate to 60 FPS

    pygame.quit()
    sys.exit()

def input_in_game(event, scene):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        scene.next_dialogue()
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        scene.prev_dialogue()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        scene.change_font_prev()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        scene.change_font_next()

if __name__ == "__main__":
    main()
