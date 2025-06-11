import pygame
from constants import *
from player import *
from asteroidfield import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field_one = AsteroidField()
    
    print(f"{updatable}")
    print(f"{drawable}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = game_clock.tick(60)/1000
        screen.fill("black")
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()