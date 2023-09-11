import pygame
from controller import InputHandler
from game_engine import GameEngine
from model import Bird, Pipe, Game
from view import Renderer

def main():
    clock, screen = initGame()

    bird = Bird()
    pipes = [Pipe()]
    game = Game()
    renderer = Renderer(screen)
    input_handler = InputHandler(bird)

    game_engine = GameEngine(bird, pipes, game, renderer, input_handler)

    while not game.game_over:
        game_engine.handle_events()
        game_engine.update()
        game_engine.render()

        pygame.display.update()
        clock.tick(60)

    quiteTheGame()

def initGame():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Flappy Bird")
    return clock,screen

def quiteTheGame():
    pygame.quit()

if __name__ == "__main__":
    main()
