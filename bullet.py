import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, settings, screen, ship):
        """Create a bullet object at ship's current position."""
        # Inherit from Sprite module
        super().__init__()
        #self.screen = screen
        
        # Create a bullet rect from scratch (no image to import)
        self.bullet_rect = pygame.Rect(
            0, 0, settings.bullet_width, settings.bullet_height)

        # Set correct position of bullet rect
        self.bullet_rect.centery = ship.bmp_rect.centery
        self.bullet_rect.right = ship.bmp_rect.right

        # Store the bullet's position as a decimal
        self.bullet_pos = float(self.bullet_rect.x)

        # Access parameter variables
        self.screen = screen
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def update(self):
        """Move bullet from left to right across screen."""
        # Update the decimal position of the bullet.
        self.bullet_pos += self.speed
        
        # Update the rect position.
        self.bullet_rect.x = self.bullet_pos

    def draw(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)
