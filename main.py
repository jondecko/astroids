# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Our main game loop boys and girls!!!
    continue_game_loop = True
    while continue_game_loop:
        # Handle an exit/close window signal
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()



if __name__ == "__main__":
    main()
