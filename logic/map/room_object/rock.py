import pygame


class Rock:
    def __init__(self, x: int, y: int):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = 'grey'

    def is_solid(self):
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)