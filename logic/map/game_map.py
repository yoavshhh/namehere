from typing import List

from logic.map.room_object.room_object import RoomObject


class GameMap:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.objects: List[RoomObject] = []

    def is_blocked(self, rect):
        for obj in self.objects:
            if obj.is_solid() and obj.rect.colliderect(rect):
                return True
        return False

    def draw(self, screen):
        for object in self.objects:
            object.draw(screen)