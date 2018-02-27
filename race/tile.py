import pygame
import os

class Tile(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        if image:
            self.image = image
            self.rect = self.image.get_rect()
    def set_image(self, filename):
        self.image = pygame.image.load(os.path.join('data',filename))
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def set_position(self, pos):
        self.rect.x, self.rect.y = pos
    def update(self,screen):
        self.draw(screen)


class Obstacle(Tile):
    def __init__(self,image):
        super().__init__(image)