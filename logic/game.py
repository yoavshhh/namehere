import pygame

from logic.map.game_map import GameMap
from logic.map.room_object.rock import Rock
from logic.player.hider import Hider
from logic.player.player import Player
from logic.player.seeker import Seeker


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.map = GameMap()
        self.map.objects.append(Rock(400, 300))
        self.seeker = Seeker(100, 100, self.map)
        self.hider = Hider(400, 100, self.map)

    def update(self):
         = self.seeker.update()
        self.hider.update()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.map.draw(self.screen)
        self.seeker.draw(self.screen)
        self.hider.draw(self.screen)

    def check_for_win(self):
        return self.seeker.shape.colliderect(self.hider.shape)
