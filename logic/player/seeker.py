import pygame
import pydantic

from logic.map.game_map import GameMap
from logic.player.player import Player



class Seeker(Player):
    def __init__(self, x, y, map: GameMap):
        super().__init__(x, y, map)
        self.color = 'blue'
        self.speed = 4


