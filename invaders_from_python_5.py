import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from alien import Alien
from bullet import Bullet
import game_functions as gf


def run_game():
    """Initialise game and create a screen object."""
    pygame.init()
    pygame.mixer.init()
    infrompy_settings = Settings()
    screen = pygame.display.set_mode(
        (infrompy_settings.screen_width, infrompy_settings.screen_height))
    pygame.display.set_caption(infrompy_settings.title)

    # Make a play button
    play_button = Button(infrompy_settings, screen, "Play")

    # Create an instance to score game stats and create a scoreboard
    stats = GameStats(infrompy_settings)
    score_board = Scoreboard(infrompy_settings, screen, stats)

    # Make a ship, group of bullets and a group of aliens
    ship = Ship(infrompy_settings=infrompy_settings, screen=screen)

    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(infrompy_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(infrompy_settings, screen, ship, bullets, stats, score_board, play_button, aliens)

        if stats.game_active:
            ship.update()
            gf.update_bullets(infrompy_settings, aliens, bullets, screen, ship, stats, score_board)
            gf.update_aliens(infrompy_settings, aliens, ship, stats, score_board, screen, bullets)
        gf.update_screen(infrompy_settings, screen, ship, aliens, bullets, stats, play_button, score_board)


run_game()
