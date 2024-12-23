import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Bullet.containers = (bullets, updateable, drawable )
    AsteroidField.containers = (updateable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for u in updateable:
            u.update(dt)
            for a in asteroids:
                if player.collision(a):
                    print("GAME OVER")
                    return
                for b in bullets:
                    if b.collision(a):
                        a.split()
                        b.kill()
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60)/1000
  

if __name__ == "__main__":
    main() 