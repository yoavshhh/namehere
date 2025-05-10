import pygame


class RoomObject:
    def __init__(self, x: int, y: int):
        self.rect = pygame.Rect(x, y, 50, 50)

    def is_solid(self):
        return False

    def draw(self, screen):
        pass