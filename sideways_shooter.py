import sys

import pygame

class SidewaysShooter:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize game and create resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Sideways Shooter")

        # Set background color
        self.bg_color = (31, 40, 45)

    def run_game(self):
        """Start the main game loop."""
        while True:
            # Watch four user input.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    # Create a game instance and run the game.
    ss = SidewaysShooter()
    ss.run_game()
