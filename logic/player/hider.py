import pygame

from logic.map.game_map import GameMap
from logic.player.key_bindings import KeyBindings
from logic.player.player import Player


class Hider(Player):
    def __init__(self, x, y, map: GameMap):
        super().__init__(x, y, map)
        self.color = 'red'
        self.speed = 8
        self.key_bindings = KeyBindings(left=pygame.K_a,
                                        right=pygame.K_d,
                                        up=pygame.K_w,
                                        down=pygame.K_s)

