"""This module holds the Ship class."""

import pygame

class Ship():
    """This is a model of a ship that shoots bullets."""

    def __init__(self, screen, settings):
        """Initialize the ship."""
        # Get game display and rocket image.
        self.screen = screen
        self.bmp = pygame.image.load('ship-left.bmp')

        # Get ship and screen rect.
        self.bmp_rect = self.bmp.get_rect()
        self.screen_rect = screen.get_rect()

        # Start rocket at center left side of screen.
        self.bmp_rect.centery = self.screen_rect.centery
        self.bmp_rect.left = self.screen_rect.left

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

        # Get ship settings.
        self.ship_settings = settings

        # Get ship's position in decimal form.
        self.bmp_position = float(self.bmp_rect.centery)

    def move(self):
        """Move the ship based on movement flags."""
        # Update ship's position, not the rect.
        if self.moving_up and self.bmp_rect.top > 0:
            self.bmp_position -= self.ship_settings.ship_speed
        if self.moving_down and self.bmp_rect.bottom < self.screen_rect.bottom:
            self.bmp_position += self.ship_settings.ship_speed

        # Update rect from position
        self.bmp_rect.centery = self.bmp_position

    def blitme(self):
        """Draw ship at current location."""
        self.screen.blit(self.bmp, self.bmp_rect)
