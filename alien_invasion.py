import sys

import pygame

from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Загальний клас, що керує песурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""
        pygame.init()
        self.settings = Settings()
        # запуск гри у повноекранному режимі
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height)) #windowed mode
        pygame.display.set_caption("Alien Invasion v.0.1a")
        self.ship = Ship(self)
        # обєднання куль та прибульців у групи
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        # задати колір фону
        self.bg_color = (230, 230, 230)
        self._create_fleet()

    def _create_fleet(self):
        """Створити флот прибульців"""
        # створити прибульця
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        #створити перший ряд прибульців
        for alien_number in range(number_aliens_x):
            #створити прибульця та поставити його до ряду
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

    def _fire_bullets(self):
        """Створюємо нову кулю та додаємо до групи куль"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Оновити позицію куль та позбавитися старих куль"""
        # оновити позиції куль
        self.bullets.update()
        # позбавитись куль шо зникли
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def run_game(self):
        """"Розпочати головний цикл гри"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Реагувати на натискання клавіш та поодії миші"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагувати на натискання клавіш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        """Реагувати, коли клавіша не натиснута"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Оновити зображення на екрані та перемикнутися на новий екран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # показати останній намальований екран
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    # створити екземпляр гри та запустити гру
    ai = AlienInvasion()
    ai.run_game()
