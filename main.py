import pygame
import sys
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")	
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    
    # groups for player
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # passing the groups on to the Player class
    Player.containers = (updatable, drawable)
    
    # group for the asteroid
    asteroids = pygame.sprite.Group()
    # passing on the groups to the Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)
    # passing on groups to the asteroid field
    AsteroidField.containers = (updatable,)
    
    # passing on the group to the Shot class
    Shot.containers = (shots, updatable, drawable)
    
    # the actual player
    player = Player(x = (SCREEN_WIDTH / 2), y = (SCREEN_HEIGHT / 2))
    # the actual asteroid field
    asteroidField = AsteroidField(color="red")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        log_state()
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen=screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                

if __name__ == "__main__":
    main()
