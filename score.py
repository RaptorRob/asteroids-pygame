import pygame
from constants import SCORE_POINTS, EXTRA_SCORE_THRESHOLD

class Score():
    def __init__(self) -> None:
        self.score = 0
        self.asteroid_count = 0
    
    def add_score(self) -> None: 
        self.asteroid_count += 1
        if (self.asteroid_count % 10) == 0:
            self.score += SCORE_POINTS + EXTRA_SCORE_THRESHOLD
        self.score += SCORE_POINTS
    
    def get_score(self) -> int:
        return self.score