import pygame
import sys
from game.setting.util import read_json_file
from game.ui import Button
from game.scene import Scene

class Menu:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Menu, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, setting):
        print(f"Menu : {self}")
        self.data = self.read()
        self.setting = setting
        self.menu_items = []
        self.current_menu = None
        self.x = 960

        Menu.instance = self

    def read(self):
        return read_json_file("game/setting/menu.json")
    
    def display(self):
        print(self.data)

    def init_menu(self):
        main_menu = "main menu"
        m = self.data[main_menu]

        menu_item = MenuItem(main_menu, None, self.setting)
        self.current_menu = menu_item
        self.menu_items.append(menu_item)
        for a in m:
            self.check_submenu(a, menu_item)

    def check_submenu(self, a, menu_item):
        
        prev_menu_item = menu_item
        new_menu_item = MenuItem(a["name"], prev_menu_item, self.setting)
        self.menu_items.append(new_menu_item)

        if a.get("submenu") is not None:
            prev_menu_item.add_button(a["name"], lambda: self.change_menu(new_menu_item))
            submenus = a["submenu"]
            for submenu in submenus:
                self.check_submenu(submenu, new_menu_item)

        elif a.get("function") is not None:
            function = getattr(self, a["function"], None)
            prev_menu_item.add_button(a["name"], function)

        elif a.get("scenes") is not None:
            prev_menu_item.add_button(a["name"], lambda: self.change_menu(new_menu_item))
            scenes = a["scenes"]
            for scene in scenes:
                def _function(path=scene["path"]):
                    Scene(self.setting, path)
                    self.setting.game_state = "game"
                new_menu_item.add_button(scene["name"], _function)
        
        else:
            prev_menu_item.add_button(a["name"], lambda: self.change_menu(new_menu_item))

    # Functions for buttons
    def change_menu(self, menu):
        self.current_menu = menu

    def change_display(self):
        if self.setting.fullscreen:
            self.setting.resize_display(1344, 756)
        else:
            self.setting.to_fullscreen()
    
    def change_font(self):
        self.setting.change_font_next()

    def draw(self, screen):
        self.current_menu.draw(screen)

    def quit_button_function(self):
        pygame.quit()
        sys.exit()

class MenuItem:
    def __init__(self, name, prev_menu=None, setting=None):
        self.name = name
        self.prev_menu = prev_menu
        self.buttons = []
        self.setting = setting
        self.x = int(setting.screen_width / 7)
        self.y = int(setting.screen_height / 4)
        self.button_image = pygame.image.load("resources/images/button.png").convert_alpha()
        self.button_image = pygame.transform.scale(self.button_image, (400, 50))

    def add_button(self, name, function=None):
        button = Button(name, self.x, self.y, self.button_image, function, self.setting)
        self.y += int(15*self.setting.multiplier)
        self.buttons.append(button)

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)