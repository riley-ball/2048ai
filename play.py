from environment import *
from state import State
from constants import *

if __name__ == "__main__":
    env = environment()
    state = env.get_init_state()
    env.render(state)
    env.perform_action(state, RIGHT)
    print("------------------")
    env.render(state)
    while True:
        action = input("Enter action: ")
        if action == "d":
            action = RIGHT
        elif action == "a":
            action = LEFT
        elif action == "w":
            action = UP
        elif action == "s":
            action = DOWN
        else:
            print("Invalid action")
            continue
        env.perform_action(state, action)
        env.render(state)