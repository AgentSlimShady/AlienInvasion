class Settings:
    """КЛас для збереження всіх налаштувань гри."""

    def __init__(self):
        """Ініціалізувати налаштування гри"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Ship settings
        self.ship_speed=1.5
        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet direction 1 означає рух праворуч -1 рух ліворуч
        self.fleet_direction = 1
