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
