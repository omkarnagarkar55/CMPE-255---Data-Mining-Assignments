class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.velocity = 0
        self.gravity = 0.5

    def jump(self):
        self.velocity = -10

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

class Pipe:
    def __init__(self):
        self.x = 800
        self.y = 0
        self.width = 100
        self.height = 200
        self.speed = 5

    def update(self):
        self.x -= self.speed

class Game:
    def __init__(self):
        self.score = 0
        self.game_over = False

    def increase_score(self):
        self.score += 1

    def check_collision(self, bird, pipes):
        # Collision detection logic
        pass
