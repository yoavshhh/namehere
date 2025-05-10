import pygame

from logic.map.game_map import GameMap
from logic.player.key_bindings import KeyBindings


class Player:
    updated: bool
    def __init__(self, x: int, y: int, map: GameMap, ):
        self.shape = pygame.Rect(x, y, 50, 50)
        self.color = 'blue'
        self.speed = 5
        self.key_bindings = KeyBindings(left=pygame.K_LEFT,
                                        right=pygame.K_RIGHT,
                                        up=pygame.K_UP,
                                        down=pygame.K_DOWN)
        self.map = map

    def update(self):
        self.updated = False
        self._update()
        if self.updated:

    def _update(self):
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.key_bindings.left]:
            self.move_axis('x', -1)
        elif keys[self.key_bindings.right]:
            self.move_axis('x', 1)

        if keys[self.key_bindings.up]:
            self.move_axis('y', -1)
        elif keys[self.key_bindings.down]:
            self.move_axis('y', 1)

    def move_axis(self, axis, direction):
        for _ in range(self.speed):
            temp_rect = self.shape.copy()
            if axis == 'x':
                temp_rect.x += direction
            else:
                temp_rect.y += direction

            if not self.map.is_blocked(temp_rect):
                self.updated = True
                if axis == 'x':
                    self.shape.x += direction
                else:
                    self.shape.y += direction
            else:
                break

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.shape)
