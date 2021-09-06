import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Клас для курування кулями, випущеними з корабля"""

    def __init__(self, ai_game):
        """Створити обєкт bullet у поточній позиції корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # створити rect кулі у (0, 0) та задати правильну позицію
        self.rect = pygame.Rect(0, 0, self.settings.screen_height, self.settings.bullet_width)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Зберігати позицію кулі як десяткове значення.
        self.y = float(self.rect.y)

    def update(self):
        """Посунути кулю нагору екраном."""
        # оновити десяткову позицію кулі
        self.y -= self.settings.bullet_speed
        # оновити позицію rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Намалювати кулю на екрані"""
        pygame.draw.rect(self.screen, self.color, self.rect)
