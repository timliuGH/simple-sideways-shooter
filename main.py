"""This module sets up the main game and event loop."""

import sys

import pygame

from settings import Settings

def run_game():
    """Set up the game objects and event loop."""
    # Initialize game and create a screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.display_width, settings.display_height))
    pygame.display.set_caption(settings.display_caption)

    # Start event loop.
    while True:
        # Listen for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw screen.
        screen.fill(settings.display_color)
        
        # Make most recently drawn screen visible.
        pygame.display.flip()

run_game()
