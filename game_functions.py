"""This module holds game functions."""

import sys

import pygame

from bullet import Bullet

def keydown_event(screen, settings, ship, event, bullets):
    """Respond to keypress."""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet in bullets group.
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def keyup_event(ship, event):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(screen, settings, ship, bullets):
    """Respond to user events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_event(screen, settings, ship, event, bullets)
        elif event.type == pygame.KEYUP:
            keyup_event(ship, event)

def update_screen(screen, settings, ship, bullets):
    """Redraw and make visible newest screen."""
    # Redraw screen.
    screen.fill(settings.display_color)

    # Redraw bullets behind ship.
    for bullet in bullets.sprites():
        bullet.draw()

    # Redraw ship.
    ship.blitme()

    # Make most recently drawn screen visible.
    pygame.display.flip()
