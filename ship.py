import pygame


class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізувати корабель та задати його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # індикатор руху
        self.moving_right = False
        self.moving_left = False

        # завантажити зображення корабля та отримати його rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # створити кожен новий корабель внизу екрана, по центру
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """намалювати корабель у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """"
        оновити поточну позицію корабля на основі
        індикатора руху
        """
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
