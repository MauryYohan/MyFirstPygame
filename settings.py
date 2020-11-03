class Settings:
    """A class to store our games settings."""

    def __init__(self):
        """Initialize our games settings and screen settings """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 250)
        self.title = "Invaders from Python"

        # Ship setting
        self.ship_speed = 4.50
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        # Alien settings
        self.alien_speed_factor = 4
        self.fleet_drop_speed = 20

        # How quickly the game speeds up
        self.speedup_scale = 1.15

        # How quickly the score levels up
        self.scoreup_scale = 10

        self.initialize_dynamic_settings()

        # Add a music and sound for the game
        hit_alien = 'sounds/hit_alien.wav'
        hit_ship = 'sounds/ship_explosion.wav'

    def initialize_dynamic_settings(self):
        """Initialize settings thats change during the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 8
        self.alien_speed_factor = 2

        # Scoring
        self.alien_points = 10

        # Show me the game informations
        self.game_information()

        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def hard_settings_for_debug(self):
        """Initialize settings thats change during the game"""
        self.ship_speed = 10
        self.bullet_speed = 50
        self.alien_speed_factor = 5

        # Scoring
        self.alien_points = 100

        # Show me the game informations
        self.game_information()

        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points += self.scoreup_scale

        # --------------- For debug only ---------------
        self.game_information()

    def game_information(self):
        print("[Ship_speed: {}, Bullet_speed: {}, Alien_speed: {}, Alien_points: {}]".format(
            self.ship_speed,
            self.bullet_speed,
            self.alien_speed_factor,
            self.alien_points)
        )
