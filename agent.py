from environment import *
from state import State
from constants import *

class Agent():
    def __init__(self, environment):
        self.environment = environment
        self.init_state = State(self.environment, [[0, 0, 0, 0] for _ in range(4)])
        self.states = {}

    def get_states(self):
        values = [0] + [2**i for i in range(1, 12)]
        self.spawn_states = {}
        # Iterate through all possible spawn states
        for x1 in range(4):
            for y1 in range(4):
                for x2 in range(4):
                    for y2 in range(4):
                        temp = self.init_state.deepcopy()
                        if x1 == x2 and y1 == y2:
                            continue
                        temp.board[x1][y1] = 2
                        temp.board[x2][y2] = 2
                        self.spawn_states[temp.__hash__()] = temp.deepcopy()
        self.states = self.spawn_states