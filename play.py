from environment import *
from state import State
from constants import *
from agent import Agent

if __name__ == "__main__":
    env = Environment()
    state = env.get_init_state()
    agent = Agent(env)
    agent.get_states()
    states = agent.states
    print(len(states))
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