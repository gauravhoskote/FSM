from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def __init__(self, id, name=None, initial=False, terminal=False):
        if id == None:
            raise TypeError('Id cannot be None')
        self.__id = id
        self.__name = name
        if initial == terminal and initial != False:
            raise Exception('A state cannot be initial as well as terminal.')
        self.__initial = initial
        self.__terminal = terminal

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_initial(self):
        return self.__initial

    def get_terminal(self):
        return self.__terminal

    @abstractmethod
    def make_state(self):
        pass

    def __repr__(self):
        return f'STATE : [id: {self.__id}, name : {self.__name}, initial: {self.__initial}, terminal: {self.__terminal}]'


class Transaction(State):
    def __init__(self, attrib1, attrib2):
        self.attrib1 = attrib1
        self.attrib2 = attrib2

    def make_state(self,state_id, state_name='',initial=False, terminal=False ):
        super().__init__(state_id, state_name, initial, terminal)

txn = Transaction('a1', 'a2')
txn.make_state(None)
