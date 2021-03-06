class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during game."""
        self.ships_left = self.ai_settings.ship_limit