import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()


Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collisioncheck(player):
                print("Game over!")
            
        for item in drawable:
            item.draw(screen)
        AsteroidField()
        pygame.display.flip()
        
        
        dt = clock.tick(60) / 1000
    
    

if __name__ == "__main__":
    main()