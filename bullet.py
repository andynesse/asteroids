import pygame

from circleshape import CircleShape
from constants import BULLET_RADIUS
class Bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#ffffff", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt