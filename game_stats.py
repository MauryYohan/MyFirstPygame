
class GameStats:
    """ Track stats for invaders from Python"""
    def __init__(self, infrompy_settings):
        self.infrompy_settings = infrompy_settings
        self.reset_stats()
        self.ships_left = 10

        # Initialize the message
        self.message_defeat = "You lost! Maybe you will have a better score after another try?"

        # Start the game in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = 100   # 29480

    def reset_stats(self):
        """Initialize stats that can change during the game. """
        self.ships_left = self.infrompy_settings.ship_limit
        self.score = 0
        self.level = 1

    def defeat_messages(self):
        if self.ships_left == 0:
            print(self.message_defeat)
