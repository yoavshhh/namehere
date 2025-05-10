import pygame

from logic.map.room import Room
from logic.player.key_bindings import KeyBindings
from logic.player.player import Player


class Hider(Player):
    def __init__(self, x, y, current_room: Room):
        super().__init__(x, y, current_room)
        self.color = 'red'
        self.speed = 8
        self.key_bindings = KeyBindings(left=pygame.K_a,
                                        right=pygame.K_d,
                                        up=pygame.K_w,
                                        down=pygame.K_s)

