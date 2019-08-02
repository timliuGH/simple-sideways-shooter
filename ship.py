"""This module holds the Ship class."""

import pygame

class Ship():
    """This is a model of a ship that shoots bullets."""

    def __init__(self, screen):
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

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def move(self):
        """Move the ship based on movement flags."""
        if self.moving_up:
            self.bmp_rect.centery -= 1
        if self.moving_down:
            self.bmp_rect.centery += 1

    def blitme(self):
        """Draw ship at current location."""
        self.screen.blit(self.bmp, self.bmp_rect)
