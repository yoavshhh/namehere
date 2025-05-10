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
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("My P2P Game")

    clock = pygame.time.Clock()
    game = Game(screen)
    net = NetworkManager()
    
    logging.info("Starting game.")

    running = True
    win = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = Game(screen)
                    win = False
        if game.check_for_win():
            win = True
        if not win:
            game.update()
            game.pull()
            game.render()
        else:
            font = pygame.font.SysFont(None, 72)
            text = font.render("YOU WIN!", True, (0, 255, 0))
            screen.blit(text, (screen.get_width() // 2 - 150, screen.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
