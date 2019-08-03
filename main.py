"""This module sets up the main game and event loop."""

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Set up the game objects and event loop."""
    # Initialize game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.display_width, settings.display_height))
    pygame.display.set_caption(settings.display_caption)

    # Create ship.
    ship = Ship(screen, settings)

    # Make a group to hold ship's bullets.
    bullets = Group()

    # Start event loop.
    while True:
        gf.check_events(screen, settings, ship, bullets)
        ship.move()
        bullets.update()
        gf.update_screen(screen, settings, ship, bullets)

run_game()
