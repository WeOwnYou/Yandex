import pygame
import os
import util

pygame.font.init()
default_font = pygame.font.Font(None, 30)

class GUI:
    def __init__(self):
        self.sprite_group = []
        self.namespace = dict()
        self.buttons = []

    def get_GUIElement_by_name(self, name):
        return self.namespace[name]

    def add(self, gr_object):
        self.sprite_group.append(gr_object)
        if gr_object.name:
            self.namespace[gr_object.name] = gr_object
        if gr_object.script:
            self.buttons.append(gr_object)

    def draw(self, screen):
        for e in self.sprite_group:
            e.draw(screen)
        # self.sprite_group.draw(screen)

    def get_event(self, pos):
        for e in self.buttons:
            if e.visible and e.rect.left < pos[0] < e.rect.right and e.rect.top < pos[1] < e.rect.bottom:
                return e


class GUIElement(pygame.sprite.Sprite):
    def __init__(self, image, script=None):
        super().__init__()
        self.script = script
        self.visible = True
        self.name = image
        self.text = None
        self.text_rect = None
        try:
            self.image = pygame.image.load(os.path.join('data', image + '.png'))
        except:
            print("UNABLE TO LOAD IMAGE", image)
        self.rect = self.image.get_rect()

    def set_position(self, pos):
        self.rect.center = pos

    def set_name(self, name):
        self.name=name

    def make_visible(self):
        self.visible = True

    def make_invisible(self):
        self.visible = False

    def on_click(self):
        return self.script()

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (self.rect.x, self.rect.y))
            if self.text:
                screen.blit(self.text, (self.text_rect.x, self.text_rect.y))

    def add_text(self, text):
        surface = default_font.render(text, 5, (0, 0, 0))
        rect = surface.get_rect()
        rect.center = self.rect.center
        self.text = surface
        self.text_rect = rect


def continue_script():
    return util.B_CONTINUE

def exit_script():
    return util.B_EXIT

def change_menu_script():
    return util.B_START

def start_game_script():
    return util.B_START_GAME

def next_map_script():
    return util.B_NEXT_MAP
def exit_to_menu_script():
    return util.B_EXIT_MENU

def init_default_GUI(screen):
    d_GUI = GUI()
    menu_overlay = GUIElement('menu_overlay')
    menu_overlay.set_position((screen.get_width() // 2, screen.get_height() // 2))
    d_GUI.add(menu_overlay)

    menu_overlay.make_invisible()
    continue_button = GUIElement('continue', continue_script)
    continue_button.set_position((menu_overlay.rect.center[0], menu_overlay.rect.top + 225))
    continue_button.make_invisible()
    d_GUI.add(continue_button)

    exit_button = GUIElement('exit_game', exit_script)
    exit_button.set_position((continue_button.rect.center[0], continue_button.rect.bottom + 250))
    exit_button.make_invisible()
    d_GUI.add(exit_button)

    exit_to_menu_b = GUIElement('exit_to_menu', exit_to_menu_script)
    exit_to_menu_b.set_position((exit_button.rect.center[0], exit_button.rect.bottom - 165))
    exit_to_menu_b.make_invisible()
    d_GUI.add(exit_to_menu_b)

    return d_GUI

def menu_GUI(screen):
    d_GUI = GUI()
    start_game_b = GUIElement('unnamed_button', change_menu_script)
    start_game_b.set_name('Start')
    start_game_b.set_position((400,400))
    start_game_b.add_text("New Game")
    d_GUI.add(start_game_b)

    start_map_b = GUIElement('unnamed_button', start_game_script)
    start_map_b.set_name('Map')
    start_map_b.set_position((400,400))
    start_map_b.add_text(util.MAP_LIST[0])
    start_map_b.make_invisible()
    d_GUI.add(start_map_b)

    next_map_b = GUIElement('unnamed_button', next_map_script)
    next_map_b.set_name('NextMap')
    next_map_b.set_position((400, 700))
    next_map_b.add_text('Next map')
    next_map_b.make_invisible()
    d_GUI.add(next_map_b)

    back_menu_map_b = GUIElement('unnamed_button',change_menu_script)
    back_menu_map_b.set_name('BackMenuMap')
    back_menu_map_b.set_position((400, 1000))
    back_menu_map_b.add_text('Back')
    back_menu_map_b.make_invisible()
    d_GUI.add(back_menu_map_b)

    end_game_b = GUIElement('unnamed_button',exit_script)
    end_game_b.set_name('End')
    end_game_b.set_position((400, 700))
    end_game_b.add_text("Exit Game")
    d_GUI.add(end_game_b)

    return d_GUI
    # [<MENU_OVERLAY>, <CONTINUE_B>, <EXIT_B>]