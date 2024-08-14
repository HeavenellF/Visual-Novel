import sys
import pygame
from game.setting import Setting
from game.scene import Scene
from game.menu import Menu
from game.ui import DialogBox

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((1344, 756), pygame.RESIZABLE)
pygame.display.set_caption("Visual Novel")

# initialize Setting
setting = Setting()

# Initialize Menu
menu = Menu(setting)
menu.init_menu()

# Initialize DialogBox
DialogBox(setting=setting)

# Initialize Scene
scene = Scene(setting, None)

# Main game loop
def main():
    running = True
    clock = pygame.time.Clock()
    

    while running:
        screen.fill((0, 0, 0))  # Fill the screen with black
        if setting.game_state == "main_menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    setting.resize_display(1344, 756)
                    setting.change_font()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    setting.to_fullscreen()
                    setting.change_font()
                input_in_main_menu(event)
            
            menu.draw(screen)
                

        elif setting.game_state == "game":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    setting.game_state = "main_menu"
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    setting.resize_display(1344, 756)
                    scene.init_dialog_box()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
                    setting.to_fullscreen()
                    scene.init_dialog_box()
                input_in_game(event, scene)
            
            scene.draw(screen)


        pygame.display.flip()         # Update the display
        clock.tick(10)                # Cap the frame rate to 30 FPS

    pygame.quit()
    sys.exit()

def input_in_game(event, scene):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        scene.next_dialog()
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        scene.prev_dialog()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        setting.change_font_prev()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        setting.change_font_next()

def input_in_main_menu(event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for button in menu.current_menu.buttons:
            if button.rect.collidepoint(event.pos):
                button.handle()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        if menu.current_menu.prev_menu is not None:
            menu.current_menu = menu.current_menu.prev_menu

if __name__ == "__main__":
    main()
