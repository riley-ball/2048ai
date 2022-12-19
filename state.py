from environment import *

class State():
    def __init__(self, environment, board):
        self.board = board
        self.environment = environment