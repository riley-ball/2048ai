from state import State
from constants import *
import random


class Environment():
    def __init__(self, seed=4321, goal=2048):
        self.board = [[0, 0, 0, 0] for _ in range(4)]
        self.init_state = State(self, self.board)
        self.seed = seed
        random.seed(self.seed)
        self.spawn_tile(self.init_state, True)
        self.spawn_tile(self.init_state, True)
        self.goal = goal

    def get_init_state(self):
        return self.init_state

    def perform_action(self, state, action):
        """Perform an action on the board and return the new state

        Args:
            state (State): State to perform action on
            action (int): action to perform

        Raises:
            Exception: Invalid action

        Returns:
            _type_: _description_
        """
        score = 0
        deepcopy = state.deepcopy()
        if action == RIGHT:
            for row, _ in enumerate(state.board):
                # Move all values to the right
                _move_right(state.board[row])
                # Merge values right
                inc_score = _merge_right(state.board[row])
                score += inc_score
                # Move all values to the right
                _move_right(state.board[row])
        elif action == LEFT:
            for row, _ in enumerate(state.board):
                # Move all values to the left  
                _move_left(state.board[row])
                # Merge values left
                inc_score = _merge_left(state.board[row])
                score += inc_score
                # Move all values to the left  
                _move_left(state.board[row])
        elif action == UP:
            # Transpose the board
            state.board = _transpose_2d_list(state.board)
            for row, _ in enumerate(state.board):
                # Move all values to the left  
                _move_left(state.board[row])
                # Merge values left
                inc_score = _merge_left(state.board[row])
                score += inc_score
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
                inc_score = _merge_right(state.board[row])
                score += inc_score
                # Move all values to the right
                _move_right(state.board[row])
            # Transpose the board back
            state.board = _transpose_2d_list(state.board)
        else:
            raise Exception("Invalid action")
        new_state = State(self, state.board)
        valid = deepcopy != new_state
        if valid:
            self.spawn_tile(state)
        return (valid, new_state, score)

    def apply_action(self, state, action):
        """Perform an action on the board and return the new state

        ONLY DIFFERENCE IS THAT THIS DOES NOT SPAWN A NEW TILE
        -- Used for getting the next state for the agent

        Args:
            state (State): State to perform action on
            action (int): action to perform

        Raises:
            Exception: Invalid action

        Returns:
            _type_: _description_
        """
        score = 0
        deepcopy = state.deepcopy()
        if action == RIGHT:
            for row, _ in enumerate(state.board):
                # Move all values to the right
                _move_right(state.board[row])
                # Merge values right
                inc_score = _merge_right(state.board[row])
                score += inc_score
                # Move all values to the right
                _move_right(state.board[row])
        elif action == LEFT:
            for row, _ in enumerate(state.board):
                # Move all values to the left  
                _move_left(state.board[row])
                # Merge values left
                inc_score = _merge_left(state.board[row])
                score += inc_score
                # Move all values to the left  
                _move_left(state.board[row])
        elif action == UP:
            # Transpose the board
            state.board = _transpose_2d_list(state.board)
            for row, _ in enumerate(state.board):
                # Move all values to the left  
                _move_left(state.board[row])
                # Merge values left
                inc_score = _merge_left(state.board[row])
                score += inc_score
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
                inc_score = _merge_right(state.board[row])
                score += inc_score
                # Move all values to the right
                _move_right(state.board[row])
            # Transpose the board back
            state.board = _transpose_2d_list(state.board)
        else:
            raise Exception("Invalid action")
        new_state = State(self, state.board)
        valid = deepcopy != new_state
        return (valid, new_state, score)

    def is_solved(self, state):
        for x in range(4):
            for y in range(4):
                if state.board[x][y] == self.goal:
                    return True
        return False

    def is_terminal(self, state):
        if self.is_solved(state):
            return True
        else:
            for tile, neighbours in matrix_neighbours(state.board):
                if tile == 0:
                    return False
                for neighbour in neighbours:
                    if tile == neighbour:
                        return False
        return True
    
    def get_empty_spaces(self, state):
        # Get a list of all empty spaces
        empty_spaces = []
        for i in range(4):
            for j in range(4):
                if state.board[i][j] == 0:
                    empty_spaces.append((i, j))
        return empty_spaces

    def get_possible_spawns(self, state):
        possible_spawns = []
        empty_spaces = self.get_empty_spaces(state)
        for space in empty_spaces:
            for val in [2, 4]:
                temp = state.deepcopy()
                temp.board[space[0]][space[1]] = val
                possible_spawns.append(temp)
        return possible_spawns


    def spawn_tile(self, state, new_game=False):
        """Spawn a new tile in a random empty space"""
        # Get a list of all empty spaces
        empty_spaces = self.get_empty_spaces(state)
        # Select a random empty space
        if not new_game:
            random.seed(state)
        new_tile = random.choice(empty_spaces)
        if new_game:
            # Spawn a 2 in the empty space
            state.board[new_tile[0]][new_tile[1]] = 2
        else:
            # Spawn a 2 or 4 in the empty space
            state.board[new_tile[0]][new_tile[1]] = random.choice([2, 4])

    def render(self, state):
        """Render 2D matrix to terminal"""
        for row in state.board:
            print(row)
        print("-----------------")


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
    score = 0
    if row[0] == row[1]:
        row[0] *= 2
        row[1] = 0
        score += row[0] 
    if row[1] == row[2]:
        row[1] *= 2
        row[2] = 0
        score += row[1]
    if row[2] == row[3]:
        row[2] *= 2
        row[3] = 0
        score += row[2]
    return score

def _merge_right(row):
    """Merge values from left to right"""
    score = 0
    if row[2] == row[3]:
        row[3] *= 2
        row[2] = 0
        score += row[3] 
    if row[1] == row[2]:
        row[2] *= 2
        row[1] = 0
        score += row[2] 
    if row[0] == row[1]:
        row[1] *= 2
        row[0] = 0
        score += row[1] 
    return score

def matrix_neighbours(matrix):
    """iterate over elements of 4x4 matrix and get its neighbours"""
    for i in range(4):
        for j in range(4):
            if i == 0:
                if j == 0:
                    neighbours = [matrix[i][j+1], matrix[i+1][j]]
                elif j == 3:
                    neighbours = [matrix[i][j-1], matrix[i+1][j]]
                else:
                    neighbours = [matrix[i][j-1], matrix[i][j+1], matrix[i+1][j]]
            elif i == 3:
                if j == 0:
                    neighbours = [matrix[i][j+1], matrix[i-1][j]]
                elif j == 3:
                    neighbours = [matrix[i][j-1], matrix[i-1][j]]
                else:
                    neighbours = [matrix[i][j-1], matrix[i][j+1], matrix[i-1][j]]
            else:
                if j == 0:
                    neighbours = [matrix[i][j+1], matrix[i-1][j], matrix[i+1][j]]
                elif j == 3:
                    neighbours = [matrix[i][j-1], matrix[i-1][j], matrix[i+1][j]]
                else:
                    neighbours = [matrix[i][j-1], matrix[i][j+1], matrix[i-1][j], matrix[i+1][j]]
            yield matrix[i][j], neighbours