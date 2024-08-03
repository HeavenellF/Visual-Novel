import sys
import pygame
from game.setting import Setting
from game.scene import Scene
from game.ui import Button


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
    create_button()

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
        for button in Button.instances:
            button.draw(screen)

        scene.draw(screen)


        pygame.display.flip()         # Update the display
        clock.tick(10)                # Cap the frame rate to 30 FPS

    pygame.quit()
    sys.exit()

def input_in_game(event, scene):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        scene.next_dialogue()
        for button in Button.instances:
            if button.rect.collidepoint(event.pos):
                button.handle()
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        scene.prev_dialogue()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        setting.change_font_prev()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        setting.change_font_next()

def create_button():
    def quit_button_function():
        pygame.quit()
        sys.exit()
    
    button_image = pygame.image.load("resources/images/button.png").convert_alpha()
    button_image = pygame.transform.scale(button_image, (200, 50))
    Button("Quit", 960, 500, button_image, quit_button_function, setting)

if __name__ == "__main__":
    main()
