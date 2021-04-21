import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import pickle
import BST
from Environment import get_actions, environment, calc_length

# variables
vehicle_number_weight = 0.5
seed = 2021

# learning variables
epsilon = 0.7
discount_factor = 1
learning_rate = 0.7
iterations = 1000
RNG = np.random.RandomState(seed)

# q value for state action pairs (in route, new_route)
q_values = BST.Node(str([]), 0)
emptyNode = BST.Node(str([]), 0)
q_value_init = 0


def get_q(state, action):
    state = str(state)
    action = str(action)
    return q_values.findval(state, emptyNode).findval(action, q_value_init)


def update_q(state, action, new_q):
    state = str(state)
    action = str(action)
    actionBST = q_values.findval(state, False)
    if not actionBST:
        actionBST = BST.Node(str([]), 0)
        q_values.insert(state, actionBST)
    actionBST.update(action, new_q)


def max_q(state):
    state = str(state)
    stateBST = q_values.findval(state, False)
    if not stateBST:
        return 0
    else:
        return stateBST.max_val()


# epsilon greedy action chooser
def next_action(state, greedy):
    def get_q_map(possible_action):
        return get_q(state, possible_action)

    possible_actions = get_actions(state)
    action_q_values = list(map(get_q_map, possible_actions))
    if RNG.uniform(0, 1) < greedy:
        return possible_actions[np.argmax(action_q_values)]
    else:
        return possible_actions[RNG.randint(0, len(possible_actions))]


# is a state is an end state
def is_end(state):
    state[-1] == "end"


# determining value of a route
def calc_value(state):
    def complete_route(route):
        finished_route = route.copy()
        finished_route.insert(0, 0)
        finished_route.append(0)
        return route

    completed_routes = list(map(complete_route, state))
    return len(state) * vehicle_number_weight * max(list(map(calc_length, completed_routes)))


def calc_mid_value(state):
    def complete_route(route):
        finished_route = route.copy()
        finished_route.insert(0, 0)
        finished_route.append(0)
        return route

    completed_routes = list(map(complete_route, state))
    return max(list(map(calc_length, completed_routes)))



valueList = []
solutionList = []
# training
def train():
    for episode in range(1, iterations):
        # start
        def start_route(point):
            return [point]
        greedy=epsilon
        if episode == iterations-1:
            greedy=1
        state = list(map(start_route, range(1, len(environment))))
        end = False
        previous_value = calc_mid_value(state)
        received_reward = 0
        # take actions until end
        while not end:
            # choose action
            action = next_action(state, greedy)
            # take action
            old_state = state
            if action == "End":
                end = True
                reward = calc_value(state) - received_reward
            else:
                state = action
                # receive reward
                new_value = calc_mid_value(state)
                reward = previous_value - new_value
                received_reward = received_reward + reward
                previous_value = new_value
            old_q_value = get_q(old_state, state)
            # calculate the temporal difference
            temporal_difference = reward + (discount_factor * max_q(state)) - old_q_value

            # update Q-value previous state, action pair
            new_q_value = old_q_value + (learning_rate * temporal_difference)
            update_q(old_state, action, new_q_value)
        valueList.append(calc_value(state))
        solutionList.append(state)
        print(episode)
    dataframe = pd.DataFrame({'iteration': range(1, iterations
                                                 ), 'value': valueList})
    actualdataframe = dataframe.rolling(20).mean()
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.set_ylabel('value')
    ax1.set_xlabel('iteration')
    ax1.plot('iteration', 'value', data=actualdataframe, marker='o', color='mediumvioletred')
    plt.show()
    with open("Policy.txt", 'xb') as save_file:
        pickle.dump(q_values, save_file)
    return [iterations, solutionList, valueList]
