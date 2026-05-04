import sys
import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    TIME)
from logger import (
    log_state,
    log_event)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Clock = pygame.time.Clock()
    dt = 0
    Player1 =  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField1 = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
              return

        screen.fill("black")
        updatable.update(dt)
        for asteroid_instance in asteroids:
            if asteroid_instance.collides_with(Player1) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(TIME) / 1000



if __name__ == "__main__":
    main()
