import sys
import pygame
from pathlib import Path
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from level import Level


class Game:
    def __init__(self):
        """Initialize the game, set up the screen and clock."""
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Sprout Land")
        self.clock = pygame.time.Clock()
        self.level = Level()

        # Load and play background music
        pygame.mixer.music.load(Path("audio/bg.mp3"))
        pygame.mixer.music.set_volume(0.3)  # Adjust volume (0.0 to 1.0)
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely

    def run(self):
        while True:
            self._handle_events()
            delta_time = self.clock.tick() / 1000
            self.level.run(delta_time)
            pygame.display.update()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()

    def _quit_game(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game_instance = Game()
    game_instance.run()
