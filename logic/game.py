import pygame
from logic.player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(100, 100)

    def update(self):
        self.player.update()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)