"""This module holds game functions."""

import sys

import pygame

def check_events(ship):
    """Respond to user events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

def update_screen(screen, settings, ship):
    """Redraw and make visible newest screen."""
    # Redraw screen.
    screen.fill(settings.display_color)
    ship.blitme()

    # Make most recently drawn screen visible.
    pygame.display.flip()
