from environment import *
from state import State
from constants import *
from mcts import *

if __name__ == "__main__":

    count = 0
    wins = 0
    losses = 0
    while count < 10:
        score = 0
        env = Environment(count, 512)
        state = env.get_init_state()
        init_node = Node(state)
        # temp = state.deepcopy()
        # env.render(state)
        # valid, new_state, score = env.perform_action(state, UP)
        # env.render(new_state)
        
        iterations = 1000
        exploration = 0.5
        mcts = MCTS(env, init_node, iterations, exploration)
        # env.render(mcts.state)
        while True:
            mcts = MCTS(env, mcts, iterations, exploration)
            if env.is_terminal(mcts.state):
                # env.render(mcts.state)
                # print("Score:", score)
                if env.is_solved(mcts.state):
                    wins += 1
                    count += 1
                    print("Solved")
                    break
                else:
                    count += 1
                    losses += 1
                    print("Game over")
                    break
            score += mcts.state.score
            # env.render(mcts.state)
    print("Wins:", wins, "Losses:", losses)