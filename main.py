# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from shot import Shot 
from asteroidfield import AsteroidField
from constants import *


def console_logging_startup_message():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


def main():
    pygame.init()
    console_logging_startup_message()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)

    player_start_x = SCREEN_WIDTH / 2
    player_start_y = SCREEN_HEIGHT / 2
    player = Player(player_start_x, player_start_y)
    field = AsteroidField()


    # Our main game loop boys and girls!!!
    continue_game_loop = True
    while continue_game_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")        

        for thing in updateable:
            thing.update(dt)
        for ast in asteroids:
            if ast.is_colliding(player):
                print("Game Over!")
                return
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
