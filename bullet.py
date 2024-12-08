from circleshape import *
from pygame import *
from constants import *

class Bullet(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,1)
    def update(self, dt):
        self.position += self.velocity * dt