import pygame

from logic.map.room_object.room_object import RoomObject


class Rock(RoomObject):
    def __init__(self, x: int, y: int):
        super(Rock, self).__init__(x, y)
        self.color = 'grey'

    def is_solid(self):
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)