class GameEngine:
    def __init__(self, bird, pipes, game, renderer, input_handler):
        self.bird = bird
        self.pipes = pipes
        self.game = game
        self.renderer = renderer
        self.input_handler = input_handler

    def handle_events(self):
        self.input_handler.handle_events()

    def update(self):
        self.bird.update()

        for pipe in self.pipes:
            pipe.update()

            if pipe.x + pipe.width < 0:
                self.pipes.remove(pipe)

            if pipe.x == self.bird.x:
                self.game.increase_score()

            if self.game.check_collision(self.bird, self.pipes):
                self.game.game_over = True

    def render(self):
        self.renderer.render(self.bird, self.pipes, self.game.score)
