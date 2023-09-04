import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = (255, 255, 255)
        self.bird_color = (255, 0, 0)
        self.pipe_color = (0, 255, 0)

    def render(self, bird, pipes, score):
        self.screen.fill(self.background_color)
        pygame.draw.rect(self.screen, self.bird_color, (bird.x, bird.y, 50, 50))

        for pipe in pipes:
            pygame.draw.rect(self.screen, self.pipe_color, (pipe.x, pipe.y, pipe.width, pipe.height))

        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, (0, 0, 0))
        self.screen.blit(text, (10, 10))
