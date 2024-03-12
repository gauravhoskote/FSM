from State import State
class StateSet:
    def get_states(self, states:list[State]):
        initial_count = 0
        initial_state = None
        terminal_count = 0
        terminal_state = None
        stateset = {}
        for state in states:
            if state.get_initial():
                initial_count += 1
                initial_state = state
            if state.get_terminal():
                terminal_count += 1
                terminal_state = state
            if state.get_id() in stateset.keys():
                raise Exception('Duplicate keys in StateSet')
            stateset[state.get_id()] = state
        if initial_count == 1 and terminal_count == 1 and initial_state != terminal_state:
            return stateset, initial_state, terminal_state
        else:
            raise Exception('States not initialized Correctly. The Stateset must have one initial state, one terminal state and both of them should be different.')

    def __init__(self, states : list[State]):
        self.__state_map, self.__initial_state, self.__terminal_state = self.get_states(states)

    def get_state_map(self):
        return self.__state_map

    def get_initial_state(self):
        return self.__initial_state

    def get_terminal_state(self):
        return self.__terminal_state



istate = State(0, initial=True)

estate = State(1, terminal=True)
state_set = StateSet([istate, estate, 1])