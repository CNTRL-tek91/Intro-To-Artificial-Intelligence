
from search import *
from itertools import *



class WolfGoatCabbage(Problem):
    def __init__(self):
        super(WolfGoatCabbage, self).__init__(frozenset({"F", "C", "G", "W"}), frozenset({}))


    def actions(self, state):
        empty_list = []
        farmer_state = {"F"}
        action_list = [farmer_state]
        if "F" in state:
            if "W" not in state and "G" not in state:
                return empty_list
            elif "G" not in state and "C" not in state:
                return empty_list
        else:
            if "W" in state and "G" in state:
                return empty_list
            elif "G" in state and "C" in state:
                return empty_list

        if "F" in state:

            for character in list(state):
                if character != "F":
                    action_list.extend([{"F", character}])
        else:
            for character in ["C", "G", "W"]:
                if character not in state:
                    new_list = []
                    new_list.extend(character)
            for x in new_list:
                action_list.extend([{"F",x}])



        new_action = []
        for action in action_list:
            new_action.append(action)
        return new_action



    def result(self, state, action):

        new = set(state)
        if "F" not in state:
            for character in action:
                new.add(character)
        else:
            for character in action:
                new.remove(character)

        return frozenset(new)

    def goal_test(self, state):
        if state == self.goal:
            return True
        else:
            return False




if __name__ == "__main__":
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)




