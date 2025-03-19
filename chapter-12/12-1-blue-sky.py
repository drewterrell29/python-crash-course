import pygame
import sys

class Blue_Sky:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 54, 168)

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

            self.clock.tick(60)
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = Blue_Sky()
    bs.run_game()