"""This modules holds the Settings class."""

class Settings():
    """This class holds game settings."""

    def __init__(self):
        """Initialize game settings."""
        # Display settings.
        self.display_width = 1200
        self.display_height = 800
        self.display_caption = "Simple Sideways Shooter"
        self.display_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 2.5

        # Bullet settings
        self.bullet_speed = 3.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
