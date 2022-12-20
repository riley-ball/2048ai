import random
import math
from constants import *

class Node:
    def __init__(self, state, parent=None):
        self.state = state  # the state represented by this node
        self.parent = parent  # the parent node of this node
        self.children = []  # a list of child nodes
        self.visits = 0  # the number of times this node has been visited
        self.wins = 0  # the number of wins that have occurred in this node

    def add_child(self, child_node):
        # Add a child node to this node
        self.children.append(child_node)
    
    def update(self, result):
        # Update the number of visits and wins for this node
        self.visits += 1
        self.wins += result
    
    def UCB1(self, exploration_parameter):
        # Calculate the UCB1 value for this node, using the given exploration parameter
        if self.visits == 0:
            return float("inf")
        return (self.wins / self.visits) + exploration_parameter * \
            (2 * math.log(self.parent.visits) / self.visits) ** 0.5
    
    def best_child(self, exploration_parameter):
        # Find the child node with the highest UCB1 value
        return max(self.children, key=lambda x: x.UCB1(exploration_parameter))

def MCTS(env, root, iterations, exploration_parameter):
    # Perform MCTS starting from the given root node, for the given number of iterations
    for i in range(iterations):
        node = root
        # Select a leaf node to expand
        while node.children:
            node = node.best_child(exploration_parameter)
        # Expand the leaf node by adding one child node for each possible action
        for action in ACTIONS:
            action_state = env.apply_action(node.state, action)
            for child_state in env.get_possible_spawns(action_state):
                child_node = Node(child_state, parent=node)
                node.add_child(child_node)
        # Simulate the game from the newly-expanded node to the end
        result = simulate(child_node.state)
        # Backpropagate the result up the tree
        while node is not None:
            node.update(result)
            node = node.parent
    # Return the child node with the most wins
    return root.best_child(0)

def simulate(env, state):
    # Simulate the game from the given state to the end, and return the result (win or loss)
    while not env.is_terminal(state):
        action = random.choice(ACTIONS)
        valid, state, score = env.perform_action(state, action)
    return 1 if env.is_solved(state) else 0