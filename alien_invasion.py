import sys

import pygame


from settings import  Settings

class AlienInvasion:
    """Загальний клас, що керує песурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion v.0.1a")
        # задати колір фону
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """"Розпочати головний цикл гри"""
        while True:
            # слідкувати за подіями клавіатури та миші
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # наново намалювати екран на кожній ітерації циклу
            self.screen.fill(self.settings.bg_color)
            # показати останній намальований екран
            pygame.display.flip()


if __name__ == '__main__':
    # створити екземпляр гри та запустити гру
    ai = AlienInvasion()
    ai.run_game()
