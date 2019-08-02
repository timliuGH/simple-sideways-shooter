"""This module sets up the main game and event loop."""

import pygame

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

    # Start event loop.
    while True:
        gf.check_events(ship)
        ship.move()
        gf.update_screen(screen, settings, ship)

run_game()
