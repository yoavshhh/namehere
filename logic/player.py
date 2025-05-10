import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)