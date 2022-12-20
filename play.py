from environment import *
from state import State
from constants import *
from agent import Agent
from mcts import *

if __name__ == "__main__":
    env = Environment()
    state = env.get_init_state()
    env.render(state)
    init_node = Node(state)
    iterations = 100
    exploration = 0.5
    mcts = MCTS(env, init_node, iterations, exploration)
    env.render(mcts.state)
    score = 0

    # 1688 @ 100, 1488 @ 200

    while True:
        mcts = MCTS(env, mcts, iterations, exploration)
        if env.is_terminal(mcts.state):
            env.render(mcts.state)
            print("Score:", score)
            print("Game over")
            break
        score += mcts.state.score
        env.render(mcts.state)