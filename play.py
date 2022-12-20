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




    # for i in states:
    #     env.render(states[i])
    #     print("-----")


    # env.render(state)
    # print("------------------")
    # # valid, state = env.perform_action(state, RIGHT)
    # # env.render(state)
    # # print(valid)
    # while True:
    #     action = input("Enter action: ")
    #     if action == "d":
    #         action = RIGHT
    #     elif action == "a":
    #         action = LEFT
    #     elif action == "w":
    #         action = UP
    #     elif action == "s":
    #         action = DOWN
    #     else:
    #         print("Invalid action")
    #         continue
    #     valid, state, score = env.perform_action(state, action)
    #     env.render(state)
    #     print("Scoring Function:", score)
    #     print(valid)