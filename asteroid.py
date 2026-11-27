import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float, color: str) -> None:
        super().__init__(x = x, y = y, radius = radius)
        self.x = x
        self.y = y
        self.color = color
    
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(\
            surface = screen, \
            color = self.color, \
            center = self.position, \
            radius = self.radius, \
            width = LINE_WIDTH \
        )

    def update(self, dt) -> None:
        self.position += (self.velocity * dt)
    
    def split(self):
        pygame.mixer.music.load("./sounds/thud.mp3")
        pygame.mixer.music.play()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        rotate_vector1 = self.velocity.rotate(random_angle)
        rotate_vector2 = self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(x = self.position.x, y = self.position.y, radius = new_radius, color= "blue")
        asteroid_2 = Asteroid(x = self.position.x, y = self.position.y, radius = new_radius, color= "orange")
        asteroid_1.velocity = rotate_vector1 * 1.2
        asteroid_2.velocity = rotate_vector2 * 1.2
