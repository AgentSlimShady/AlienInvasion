class GameStats:
    """Відстежування статистики гри"""

    def __init__(self,ai_game):
        """Ініціалізація статисстики"""
        self.settings=ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Ініціалізація статистики що може здійснюватись впродовж гри"""
        self.ships_left = self.settings.ship_limit