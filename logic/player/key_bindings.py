from typing import NamedTuple

import pygame


class KeyBindings(NamedTuple):
    left: int = pygame.K_LEFT
    right: int = pygame.K_RIGHT
    up: int = pygame.K_UP
    down: int = pygame.K_DOWN

