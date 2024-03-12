from State import State
from StateSet import StateSet

class FSM:
    def __init__(self, state_set:StateSet):
        self.__state_set = state_set
        self.__current_state = self.__state_set.get_initial_state()
        self.__components = None
        self.__transitions = {}

    def get_state_set(self):
        return self.__state_set

    def get_current_state(self):
        return self.__current_state

    def get_components(self):
        return self.__components

    def get_transitions(self):
        return self.__transitions


    def create_transition(self, from_id, to_id, inp='null'):
        if from_id not in self.__transitions.keys():
            self.__transitions[from_id] = {inp : to_id}
        else:
            self.__transitions[from_id][inp] = to_id

    def transition(self, inp='null'):
        try:
            self.__current_state = self.__state_set.get_state_map()[self.__transitions[self.__current_state.get_id()][inp]]
        except:
            raise Exception('Transition for the given input does not exist')


istate = State(0, initial=True)

estate = State(1, terminal=True)
state_set = StateSet([istate, estate])
fsm = FSM(state_set)

fsm.create_transition(0,1)
print(fsm.get_transitions())

print(fsm.get_current_state())
fsm.transition()
print(fsm.get_current_state())