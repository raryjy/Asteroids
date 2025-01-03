# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # set clock to control the framerate
    clock = pygame.time.Clock()
    dt = 0
    
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()   
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
 
    # player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # asteroids
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroids_field = AsteroidField()

    # shots
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                    

        screen.fill("black")

        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
