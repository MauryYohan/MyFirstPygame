import sys
import pygame
from settings import Settings


def run_game():
    """Initialise game and create a screen object."""
    pygame.init()
    infrompy_settings = Settings()

    screen = pygame.display.set_mode(
        (infrompy_settings.screen_width, infrompy_settings.screen_height))
    pygame.display.set_caption(infrompy_settings.title)

    # Start the main loop for the game

    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass trought the loop
        screen.fill(infrompy_settings.bg_color)

        # Make the most recently drawn screen visible
        pygame.display.flip()


run_game()
