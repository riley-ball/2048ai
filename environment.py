from state import State
from constants import *
import random

class environment():
    def __init__(self):
        self.board = [[0, 0, 0, 0] for _ in range(4)]
        self.init_state = State(self, self.board)
        self.spawn_tile(self.init_state)
        self.spawn_tile(self.init_state)


    def get_init_state(self):
        return self.init_state

    def perform_action(self, state, action):
        """Perform an action on the board and return the new state"""
        if action == RIGHT:
            for row, _ in enumerate(state.board):
                # Move all values to the right
                _move_right(state.board[row])
                # Merge values right
                _merge_right(state.board[row])
                # Move all values to the right
                _move_right(state.board[row])
        elif action == LEFT:
            for row, _ in enumerate(state.board):
                # Move all values to the left  
                _move_left(state.board[row])
                # Merge values left
                _merge_left(state.board[row])
                # Move all values to the left  
                _move_left(state.board[row])
        elif action == UP:
            # Transpose the board
            state.board = _transpose_2d_list(state.board)
            for row, _ in enumerate(state.board):
                # Move all values to the left  
                _move_left(state.board[row])
                # Merge values left
                _merge_left(state.board[row])
                # Move all values to the left  
                _move_left(state.board[row])
            # Transpose the board back
            state.board = _transpose_2d_list(state.board)
        elif action == DOWN:
            # Transpose the board
            state.board = _transpose_2d_list(state.board)
            for row, _ in enumerate(state.board):
                # Move all values to the right
                _move_right(state.board[row])
                # Merge values right
                _merge_right(state.board[row])
                # Move all values to the right
                _move_right(state.board[row])
            # Transpose the board back
            state.board = _transpose_2d_list(state.board)
        else:
            raise Exception("Invalid action")
        self.spawn_tile(state)
        return State(self, state.board)

    def is_solved(self, state):
        
        for i in state.board:
            for j in state.board:
                if j == 2048:
                    return True
        return False

    def spawn_tile(self, state):
        """Spawn a new tile in a random empty space"""
        # Get a list of all empty spaces
        empty_spaces = []
        for i in range(4):
            for j in range(4):
                if state.board[i][j] == 0:
                    empty_spaces.append((i, j))
        # Select a random empty space
        new_tile = random.choice(empty_spaces)
        # Spawn a 2 or 4 in the empty space
        state.board[new_tile[0]][new_tile[1]] = random.choice([2, 4])

    def render(self, state):
        """Render 2D matrix to terminal"""
        for row in state.board:
            print(row)


def _transpose_2d_list(matrix):
    return [list(row) for row in zip(*matrix)]

def _move_left(row):
    """Move all values to the left"""
    for i in range(1, 4):
        if row[i]:
            for j in range(i, 0, -1):
                if not row[j - 1]:
                    row[j - 1] = row[j]
                    row[j] = 0
                else:
                    break
    return row

def _move_right(row):
    """Move all values to the right"""
    for i in range(2, -1, -1):
        if row[i]:
            for j in range(i, 3):
                if not row[j + 1]:
                    row[j + 1] = row[j]
                    row[j] = 0
                else:
                    break
    return row

def _merge_left(row):
    """Merge values from right to left"""
    if row[2] == row[3]:
        row[2] *= 2
        row[3] = 0
    if row[1] == row[2]:
        row[1] *= 2
        row[2] = 0
    if row[0] == row[1]:
        row[0] *= 2
        row[1] = 0
    return row

def _merge_right(row):
    """Merge values from left to right"""
    if row[0] == row[1]:
        row[1] *= 2
        row[0] = 0
    if row[1] == row[2]:
        row[2] *= 2
        row[1] = 0
    if row[2] == row[3]:
        row[3] *= 2
        row[2] = 0
    return row