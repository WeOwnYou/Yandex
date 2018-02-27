import  pygame
import os
import math
from PIL import Image
VELOCITY = 20


class Car(pygame.sprite.Sprite):
    def __init__(self,image):
        super().__init__()
        self.vel = 0
        self.svel = VELOCITY
        self.image_name = image
        self.clock = pygame.time.Clock()
        self.rotation=0
        try:
            self.image=pygame.image.load(os.path.join('data',image+'.png'))
        except:
            print('UNABLE TO LOAD IMAGE '+image)
        self.rect = self.image.get_rect()
        self.start_x = 200
        self.start_y = 200

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))

    def update(self, screen, rotation_turn, entities, rotating, accelerating, steering):
        if not pygame.sprite.spritecollideany(self, entities):
            pygame.time.wait(1000)
            self.rect.x = self.start_x
            self.rect.y = self.start_y
            self.rotation=0
            self.vel = 0
        if rotating:
            self.rotation += rotation_turn
        if rotating and abs(self.vel) == 0: # НЕ поворачиваем если стоим на месте
            self.rotation -= rotation_turn
        if accelerating and abs(self.vel) < self.svel and not rotating:  # Разгоняемся
            self.vel += 0.05 * self.svel
            if steering:
                self.vel *= 0.5
        if rotating and accelerating and abs(self.vel) < self.svel: # Разгоняемся на повороте(чуть медленнее)
            self.vel += 0.02 * self.svel
            if steering:
                self.vel *= 0.5
        if not accelerating and self.vel > 0:  # Тормозим
            self.vel -= self.svel * 0.04 + steering * 0.03 * self.svel
            #   print('stopped')
        if not steering and self.vel < 0:  # Тормозим когда едем назад
            self.vel *= 0.5
        if steering and self.vel <= 0:  # Едем назад
            self.vel = - self.svel * 0.3
        if -0.0001 < self.vel < 0.00001: # Избавляемся от дроби в скорости
            self.vel = 0
        self.rotate(self.rotation)
        self.rect.x += self.vel * math.cos(self.rotation * (math.pi / 180.0))
        self.rect.y -= self.vel * math.sin(self.rotation * (math.pi / 180.0))

    def set_image(self,image):
        try:
            self.image=pygame.image.load(os.path.join('data',image+'.png'))
        except:
            print('UNABLE TO LOAD IMAGE '+image)
            raise EnvironmentError

    def rotate(self, value):
        image = Image.open(os.path.join('data',self.image_name+'.png'))
        image_out = image.rotate(value)
        image_out.save(os.path.join('data',self.image_name+'t.png'))
        self.set_image(self.image_name+'t')