import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode(( SCREEN_WIDTH, SCREEN_HEIGHT ))

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Bullet.containers = (updatables, drawables, bullets)

    asteroid_field = AsteroidField()
    player = Player( SCREEN_WIDTH/2, SCREEN_HEIGHT/2 )
    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatables.update(dt)

        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.circle_collision(bullet):
                    asteroid.split()
                    bullet.kill()

            if asteroid.circle_collision(player):
                sys.exit("Game Over!")

        screen.fill("#000000")
        for obj in drawables:
            obj.draw(screen)
        
        dt = clock.tick(60)/1000
        pygame.display.flip()



if __name__ == "__main__":
    main()
