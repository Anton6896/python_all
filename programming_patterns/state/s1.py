from enum import Enum, auto
from dataclasses import dataclass
from operator import add
from operator import floordiv
from operator import mul
from operator import sub


@dataclass(slots=True)
class Number:
    value: float


@dataclass(slots=True)
class Action:
    type_of: str

    def get_action(self):
        return {
            '+': add,
            '-': sub,
            '*': mul,
            '/': floordiv,
        }.get(self.type_of) or add

    @staticmethod
    def get_available_actions():
        return ('+', '-', '*', '/', '(', ')')

    @property
    def is_add(self):
        return self.type_of == '+'



class Calculator:
    class State(Enum):
        TOKENIZE = auto()
        HANDLE_PRENTICES = auto()
        HANDLE_MUL_DIV = auto()
        HANDLE_ADD_SUB = auto()
        FAILURE = auto()
        CONCLUSION = auto()

    AVAILABLE_ACTIONS = ('+', '-', '*', '/', '(', ')')

    def __init__(self, expression: str) -> None:
        self.expression = expression
        self.state = None
        self.response = None
        self.calculation_state: list[Action | Number] = []

    def run(self):
        try:
            self.tokenize()
            self._run()
            return self.response or self.expression
        except Exception as e:  # todo
            raise

    def tokenize(self) -> list:
        self.state = self.State.TOKENIZE
        holder = ''
        for ch in self.expression:
            if ch in Action.get_available_actions():
                try:
                    if holder.strip():
                        self.calculation_state.append(
                            Number(float(holder.strip())))
                except ValueError:
                    self.state = self.State.FAILURE
                    raise Exception(
                        'its not math expression: ' + self.expression)

                self.calculation_state.append(Action(ch))
                holder = ''
            else:
                holder += ch

        if holder.strip():
            self.calculation_state.append(Number(float(holder.strip())))

    def _run(self):
        print('initial state: ', self.calculation_state)

        while self.state not in [self.State.FAILURE, self.State.CONCLUSION]:
            print('loop -------')
            have_actions = False

            for idx, token in enumerate(self.calculation_state):

                if isinstance(token, Action) and token.is_add:
                    have_actions = True
                    self.handle_add(idx, token, self.calculation_state)
                    print('result: ', self.calculation_state)
                    break

                    

            if not have_actions:
                self.state = self.State.CONCLUSION

    def handle_add(self, idx, token: Action, current_state: list):
        left = current_state[idx - 1]
        right = current_state[idx + 1]
        result = token.get_action()(left.value, right.value)
        print('handle_add:', left, right, result)

        self.update_calculation_state(result, idx - 1, idx + 1)

    def update_calculation_state(self, result: float, left: int, right: int):
        new_state = []

        if (left - 1) > 0:
            new_state.extend(self.calculation_state[::(left - 1)])

        new_state.append(Number(result))

        if right + 1 <= len(self.calculation_state):
            new_state.extend(self.calculation_state[(right + 1)::])

        self.calculation_state = new_state
        del new_state


if __name__ == '__main__':
    # expression = '10 + 2 / ( 4 - 1) + 5'
    expression = '10 + 2 + 1'

    c = Calculator(expression).run()
