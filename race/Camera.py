import pygame
bgColor= (255,255,255)
game_loop=1
#WIN_WIDTH=800
#WIN_HEIGHT=640
resolution=tuple((800,640))
WALL_WIDTH = 32
WALL_HEIGHT = 32
WALL_COLOR ="#FF6262"
MOVE_SPEED=8

class Camera(object):
    def __init__(self, camera_func, width, height, win_width, win_height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
        self.win_height = win_height
        self.win_width = win_width
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect, self.win_width, self.win_height)


def camera_configure(camera, target_rect, win_width, win_height):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+win_width / 2, -t+win_height / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-win_width), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-win_height), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы
    return pygame.Rect(l, t, w, h)