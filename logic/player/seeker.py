import pygame
import pydantic

from logic.map.room import Room
from logic.player.player import Player



class Seeker(Player):
    def __init__(self, x, y, current_room: Room):
        super().__init__(x, y, current_room)
        self.color = 'blue'
        self.speed = 4


