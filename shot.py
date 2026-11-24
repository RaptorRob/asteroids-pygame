import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float, color: str) -> None:
        super().__init__(x = x, y = y, radius = radius)
        self.shot_radius = SHOT_RADIUS
        self.color = color
    
    def draw(self, screen: pygame.surface) -> None:
        pygame.draw.circle(\
                    surface = screen, \
                    color = self.color, \
                    center = self.position, \
                    radius = self.radius, \
                    width = LINE_WIDTH \
                )
    
    def update(self, dt) -> None:
            self.position += (self.velocity * dt)
    