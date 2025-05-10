import pygame

from logic.map.game_map import GameMap
from logic.map.room_object.rock import Rock
from logic.player.hider import Hider
from logic.player.player import Player
from logic.player.seeker import Seeker


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.map = GameMap(4, 4)
        first_room = self.map.rooms[0][0]
        first_room.objects.append(Rock(400, 300))
        self.seeker = Seeker(100, 100, first_room)
        self.hider = Hider(400, 100, first_room)

    def update(self):
        self.seeker.update()
        self.hider.update()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.seeker.current_room.draw(self.screen)
        self.seeker.draw(self.screen)
        self.hider.draw(self.screen)