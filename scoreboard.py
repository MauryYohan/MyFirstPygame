import pygame
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """A class to store and show scoring informations."""
    def __init__(self, infrompy_settings, screen, stats):
        """Initialize score attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.infrompy_settings = infrompy_settings
        self.stats = stats

        # Font settings for score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Font settings for high score
        self.high_text_color = (255, 30, 30)
        self.high_font = pygame.font.SysFont(None, 48)

        # Prepare a few variables
        self.high_score_image = ''
        self.high_score_rect = ''

        self.score_image = ''
        self.score_rect = ''

        self.level_image = ''
        self.level_rect = ''

        # Prepare the initial score image
        self.prep_level()
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()

    def prep_level(self):
        """ Turn the level into a rendered image. """
        level_str = "Level: "
        if self.stats.level > 1:
            level_str = "Levels: "
        str_level = str(self.stats.level)
        level_str += str_level

        self.level_image = self.font.render(level_str, True, self.text_color, self.infrompy_settings.bg_color)

        # Display the score in the top left of the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = 140
        self.level_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        # Prepare the initial high score image
        high_score_str = "High Score: "
        str_high_score = str(self.stats.high_score)
        high_score_str += str_high_score
        self.high_score_image = self.font.render(high_score_str, True, self.high_text_color, self.infrompy_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()

        # If you wanna want to have it at the center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_score(self):
        """Turn the score into a rendered image."""
        # Prepare the initial score image
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.infrompy_settings.bg_color)
        self.score_rect = self.score_image.get_rect()

        # Display the score in the top right of the screen
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the levels, high_score and the score to the screen"""
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.score_image, self.score_rect)

        # Draw ships
        self.ships.draw(self.screen)

    def prep_ships(self):
        """ Show how many lives we have left """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.infrompy_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
