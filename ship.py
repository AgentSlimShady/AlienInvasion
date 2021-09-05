import pygame


class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # завантажити зображення корабля та отримати його rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # створити кожен новий корабель внизу екрана, по центру
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """намалювати корабель у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)
