import pygame
import logging
import sys

from logic.game import Game
from net.network_manager import NetworkManager

# Setup logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler("game.log"),
        logging.StreamHandler(sys.stdout)  # Also prints to console
    ]
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My P2P Game")

    clock = pygame.time.Clock()
    game = Game(screen)
    net = NetworkManager()
    
    logging.info("Starting game.")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        game.render()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
