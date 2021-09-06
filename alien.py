import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас, що представляє одного прибульця з флоту"""
    def __init__(self, ai_game):
        """Ініціалізувати прибульця та задати його початкове розташування"""
        super().__init__()
        self.screen = ai_game.screen

        #завантажити зображеня прибульця та втсановити його rect атрибут
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #створювати кожного нового прибульця з лівого краю верху екрану
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        #зберегти правильну горизонтальну позицію прибульців
        self.x=float(self.rect.x)
