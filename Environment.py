import CoordinateConverter

max_vehicles = 2
coordinates = "belgium-d1-n30"
environment = CoordinateConverter.convert("datasets/"+coordinates)
depot = int(0)


# find all actions that can be taken from current state
def get_actions(state):
    def new_state(group1, group2):
        def merge_group(todo1, todo2, result, previous):
            if todo2 and not todo1:
                result.extend(todo2)
            elif todo1 and not todo2:
                result.extend(todo1)
            if not todo1 or not todo2:
                return result
            previous_todo1 = environment[previous][todo1[0]]
            previous_todo2 = environment[previous][todo2[0]]
            if previous_todo1 < previous_todo2:
                result.append(todo1[0])
                return merge_group(todo1[1:], todo2, result, todo1[0])
            else:
                result.append(todo2[0])
                return merge_group(todo1, todo2[1:], result, todo2[0])

        actions = []
        if len(state) > 2:
            for group in state:
                if not ((group == group1) or (group == group2)):
                    actions.append(group)
            if get_length(depot, group1[0]) > get_length(depot, group2[0]):
                actions.append(merge_group(group1, group2[1:], [group2[0]], group2[0]))
            else:
                actions.append(merge_group(group1[1:], group2, [group1[0]], group1[0]))
        else:
            if get_length(depot, group1[0]) > get_length(depot, group2[0]):
                actions = [merge_group(group1, group2[1:], [group2[0]], group2[0])]
            else:
                actions = [merge_group(group1[1:], group2, [group1[0]], group1[0])]
        return sorted(actions, key=lambda x: x[0])

    result = []
    if len(state) > 1:
        for ref1 in range(len(state)):
            group1 = state[ref1]
            for ref2 in range(ref1):
                group2 = state[ref2]
                if not group1 == group2:
                    result.append(new_state(group1, group2))
        if len(state) <= max_vehicles:
            result.append("End")
    else:
        result = ["End"]
    return result


# get length of a route
def get_length(A, B):
    return environment[A][B]


def calc_length(route):
    def length_loop(ref, length):
        if ref >= len(route):
            return length + get_length(route[ref - 1], depot)
        else:
            return length_loop(ref + 1, length + get_length(route[ref - 1], route[ref]))

    if not route:
        return 0
    else:
        return length_loop(1, 0)
