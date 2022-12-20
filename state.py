from environment import *

class State():
    def __init__(self, environment, board):
        self.board = board
        self.environment = environment

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def deepcopy(self):
        return State(self.environment, [row[:] for row in self.board])

    def get_successors(self):
        successors = []
        for action in [UP, DOWN, LEFT, RIGHT]:
            valid, state, score = self.environment.apply_action(self.deepcopy(), action)
            if valid:
                successors.append(state)
        return successors