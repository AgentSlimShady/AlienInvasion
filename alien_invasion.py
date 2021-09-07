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
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2*alien_width)
        # визначити, яка кількість рядів прибульців поиіщається на екрані
        ship_height=self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height)-ship_height)
        number_rows = available_space_y // (2*alien_height)
        #створити повний флот прибульців
        for row_number in range (number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)

    def _create_alien(self, alien_number, row_number):
            #створити прибульця та поставити його до ряду
            alien = Alien(self)
            alien_width, alien_height = alien.rect.size
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
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
        # ПЕРЕВІТИти чи котрась з куль не влучила в прибульця
        # якщо так то позбавитись і кулі і прибульцяґ
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def run_game(self):
        """"Розпочати головний цикл гри"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self._update_aliens()

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

    def _update_aliens(self):
        """Оновоити позиції всіх приульців у флоті"""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """
        Реагує відповідно до того, чи досяг котрийсь
        із прибульців краю екрана.
        :return:
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Спуск всього флоту та зміна його напрямку"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    # створити екземпляр гри та запустити гру
    ai = AlienInvasion()
    ai.run_game()
