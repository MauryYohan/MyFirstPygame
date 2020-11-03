import sys
from time import sleep

import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, infrompy_settings, screen, ship, bullets, stats):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_p:
        if stats.game_active:
            stats.game_active = False
        else:
            stats.game_active = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(infrompy_settings, screen, ship)
        # Keep the last bullet in a variable
        last_newbullet = new_bullet
        last_newbullet.stop_sounds()
        new_bullet.play_sounds()
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to keyup release."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(infrompy_settings, screen, ship, bullets, stats, score_board, play_button, aliens):
    # Respond to key presses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(
                event, infrompy_settings, screen, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(
                infrompy_settings, screen, stats, score_board, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(infrompy_settings, screen, stats, score_board, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    # Start a new game when the button is clicked
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:

        # Reset the game settings
        infrompy_settings.initialize_dynamic_settings()
        # infrompy_settings.hard_settings_for_debug()

        # Hide the mouse
        pygame.mouse.set_visible(False)

        # Reset the game stats
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        score_board.prep_score()
        score_board.prep_level()
        score_board.prep_level()
        score_board.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(infrompy_settings, screen, ship, aliens)
        ship.center_ship()




def update_screen(infrompy_settings, screen, ship, aliens, bullets, stats, play_button, score_board):
    """ Update the images on the screen and flip to the new screen"""
    # Redraw the screen during each pass trought the loop
    screen.fill(infrompy_settings.bg_color)

    # Redraw all bullets behind the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Draw the scoreboard info
    score_board.show_score()

    # Draw the level info
    score_board.prep_level()

    # Draw the play button when the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(infrompy_settings, aliens, bullets, screen, ship, stats, score_board):
    """ Update position of bullets and remove old bullets """
    bullets.update()

    # Remove bullets that have left our game screen.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check collision between aliens and bullet
    check_bullet_alien_collision(infrompy_settings, aliens, bullets, screen, ship, stats, score_board)


def check_bullet_alien_collision(infrompy_settings, aliens, bullets, screen, ship, stats, score_board):
    """Respond to bullet-alien collision"""
    # Update bullets positions
    # Remove any bullets and aliens that have collisions.
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for aliens in collision.values():
        stats.score += infrompy_settings.alien_points * len(aliens)
        score_board.prep_score()
    check_high_score(stats, score_board)
        #-- DEBUG print(infrompy_settings.alien_points, " added")
    if len(aliens) == 0:
        # Destroy existing bullet, speed up the game, level up and create a new fleet
        bullets.empty()
        infrompy_settings.increase_speed()
        # Increase level
        stats.level += 1
        score_board.prep_level()
        create_fleet(infrompy_settings, screen, ship, aliens)


def create_fleet(infrompy_settings, screen, ship, aliens):
    """ Create a fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between aliens is equal to one alien width
    alien = Alien(infrompy_settings, screen)
    number_alien_x = get_number_aliens_x(infrompy_settings, alien.rect.width)
    number_rows = get_number_rows(infrompy_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(infrompy_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(infrompy_settings, alien_width):
    """How many aliens will fit in a row."""
    available_space_x = infrompy_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (1 * alien_width))
    return number_aliens_x


def create_alien(infrompy_settings, screen, aliens, alien_number, row_number):
    """ Create an alien and place it in a row """
    alien = Alien(infrompy_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.y + 1 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(infrompy_settings, ship_height, alien_height):
    """ Determine the number of rows of aliens that fit on the screen. """
    available_space_y = (infrompy_settings.screen_height - (1 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(infrompy_settings, aliens):
    """ Respond if any aliens have reched the edge of the screen. """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(infrompy_settings, aliens)
            break


def change_fleet_direction(infrompy_settings, aliens):
    """ Drop the fleet and change the fleets directions. """
    for alien in aliens.sprites():
        alien.rect.y += infrompy_settings.fleet_drop_speed
    infrompy_settings.fleet_direction *= -1


def ship_hit(infrompy_settings, stats, score_board, screen, ship, aliens, bullets):
    """Respond to a ship being hit by an alien."""
    if stats.ships_left > 0:
        # Decrement ships_left
        stats.ships_left -= 1
        print("Life remain: ", stats.ships_left + 1)

        # Empty the list of aliens ans bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        create_fleet(infrompy_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    elif stats.ships_left == 0:
        stats.defeat_messages()
        stats.game_active = False
        # pygame.mouse.set_visible(True)

def check_aliens_bottom(infrompy_settings, stats, score_board, screen, ship, aliens, bullets):
    """ Check if aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(infrompy_settings, stats, score_board, screen, ship, aliens, bullets)
            break


def update_aliens(infrompy_settings, aliens, ship, stats, score_board, screen, bullets):
    """ Check if the fleet has reached the edge and then update the position of all aliens """
    check_fleet_edges(infrompy_settings=infrompy_settings, aliens=aliens)
    aliens.update()

    # Look for alien-ship colision
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Your ship has been hit")
        ship_hit(infrompy_settings, stats, score_board, screen, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen
    check_aliens_bottom(infrompy_settings, stats, score_board, screen, ship, aliens, bullets)


def check_high_score(stats, score_board):
    """ Check to see if there is a new high score """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()
