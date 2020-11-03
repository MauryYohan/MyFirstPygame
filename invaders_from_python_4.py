import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Initialise game and create a screen object."""
    pygame.init()
    infrompy_settings = Settings()
    screen = pygame.display.set_mode(
        (infrompy_settings.screen_width, infrompy_settings.screen_height))
    pygame.display.set_caption(infrompy_settings.title)

    # Create a ship
    ship = Ship(infrompy_settings=infrompy_settings, screen=screen)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ship=ship)
        ship.update()
        gf.update_screen(settings=infrompy_settings, screen=screen, ship=ship)


run_game()
