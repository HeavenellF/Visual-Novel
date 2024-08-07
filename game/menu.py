import pygame
import sys
from game.setting.util import read_json_file
from game.ui import Button

class Menu:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Menu, cls).__new__(cls)
        return cls.instance
    
    def __init__(self, setting):
        self.data = self.read()
        self.setting = setting
        self.menu_items = []
        self.current_menu = None
        self.x = 960
        self.y = 25

        Menu.instance = self

    def read(self):
        return read_json_file("game/setting/menu.json")
    
    def display(self):
        print(self.data)

    def init_menu(self):
        main_menu = "main menu"
        m = self.data[main_menu]

        menu_item = MenuItem(main_menu)
        self.current_menu = menu_item
        self.menu_items.append(menu_item)
        for a in m:
            self.check_submenu(a, menu_item)

    def check_submenu(self, a, menu_item):
        button_image = pygame.image.load("resources/images/button.png").convert_alpha()
        button_image = pygame.transform.scale(button_image, (200, 50))
        
        prev_menu_item = menu_item
        new_menu_item = MenuItem(a["name"], prev_menu_item)
        self.menu_items.append(new_menu_item)

        if a.get("submenu") is not None:
            prev_menu_item.add_button(a["name"], self.x, self.y, button_image, lambda: self.change_menu(new_menu_item), self.setting)
            self.y += 50
            submenus = a["submenu"]
            for submenu in submenus:
                self.check_submenu(submenu, new_menu_item)

        elif a.get("function") is not None:
            function = getattr(self, a["function"], None)
            prev_menu_item.add_button(a["name"], self.x, self.y, button_image, function, self.setting)
            self.y += 50

        elif a.get("scenes") is not None:
            prev_menu_item.add_button(a["name"], self.x, self.y, button_image, lambda: self.change_menu(new_menu_item), self.setting)
            self.y += 50
            scenes = a["scenes"]
            for scene in scenes:
                new_menu_item.add_button(scene["name"], self.x, self.y, button_image, None, self.setting)
                self.y += 50
        
        else:
            prev_menu_item.add_button(a["name"], self.x, self.y, button_image, lambda: self.change_menu(new_menu_item) , self.setting)
            self.y += 50

    def change_menu(self, menu):
        self.current_menu = menu
        print(self.current_menu.name)

    def draw(self, screen):
        self.current_menu.draw(screen)

    def quit_button_function(self):
        pygame.quit()
        sys.exit()

class MenuItem:
    def __init__(self, name, prev_menu=None):
        self.name = name
        self.prev_menu = prev_menu
        self.buttons = []

    def add_button(self, name, x, y, image, function=None, setting=None):
        button = Button(name, x, y, image, function, setting)
        self.buttons.append(button)

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)