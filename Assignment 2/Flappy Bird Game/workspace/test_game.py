import pytest
from model import Bird, Pipe, Game

def test_bird_jump():
    bird = Bird()
    initial_velocity = bird.velocity
    bird.jump()
    assert bird.velocity == initial_velocity - 10

def test_pipe_update():
    pipe = Pipe()
    initial_x = pipe.x
    pipe.update()
    assert pipe.x == initial_x - pipe.speed

def test_game_increase_score():
    game = Game()
    initial_score = game.score
    game.increase_score()
    assert game.score == initial_score + 1

def test_game_check_collision():
    game = Game()
    bird = Bird()
    pipes = [Pipe()]
    assert not game.check_collision(bird, pipes)
    # Add collision test cases

def test_game_update():
    game = Game()
    initial_score = game.score
    game.update()
    assert game.score == initial_score + 1


