"""This module holds game functions."""

import sys

import pygame

def check_events():
    """Respond to user events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, settings, ship):
    """Redraw and make visible newest screen."""
    # Redraw screen.
    screen.fill(settings.display_color)
    ship.blitme()

    # Make most recently drawn screen visible.
    pygame.display.flip()
