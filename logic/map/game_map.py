from typing import List

import pygame

from logic.map.room import Room


class GameMap:
    def __init__(self, width=4, height=4):
        self.width = width
        self.height = height
        self.rooms = [[Room() for _ in range(width)] for _ in range(height)]


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)