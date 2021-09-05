import sys

import pygame

from ship import Ship
from settings import Settings


class AlienInvasion:
    """Загальний клас, що керує песурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion v.0.1a")
        self.ship = Ship(self)
        # задати колір фону
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """"Розпочати головний цикл гри"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Реагувати на натискання клавіш та поодії миші"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Оновити зображення на екрані та перемикнутися на новий екран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # показати останній намальований екран
        pygame.display.flip()


if __name__ == '__main__':
    # створити екземпляр гри та запустити гру
    ai = AlienInvasion()
    ai.run_game()
