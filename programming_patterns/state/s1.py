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
        return '+', '-', '*', '/'

    @property
    def is_priority_action(self) -> bool:
        return self.type_of in ('*', '/')


class Calculator:
    class State(Enum):
        TOKENIZE = auto()
        HANDLE_PRENTICES = auto()
        HANDLE_MUL_DIV = auto()
        HANDLE_ADD_SUB = auto()
        FAILURE = auto()
        CONCLUSION = auto()

    def __init__(self, expression: str) -> None:
        self.expression = expression
        self.state = None
        self.response = None
        self.calculation_state: list[Action | Number] = []

    def run(self):
        try:
            self.tokenize()
            self._run()
            if self.calculation_state:
                self.response = self.calculation_state[0].value
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

            idx = 0
            while idx < len(self.calculation_state):
                token = self.calculation_state[idx]
                if isinstance(token, Action) and token.is_priority_action:
                    have_actions = True
                    self.handle_action(idx, token)
                    idx -= 1
                else:
                    idx += 1

            idx = 0
            while idx < len(self.calculation_state):
                token = self.calculation_state[idx]
                if isinstance(token, Action):
                    have_actions = True
                    self.handle_action(idx, token)
                    idx -= 1
                else:
                    idx += 1

            if not have_actions:
                self.state = self.State.CONCLUSION

    def do_calculation(self, start, end) -> int:
        for i in range(start, end):
            token = self.calculation_state[i]

    def handle_action(self, idx, action: Action):
        left_idx = idx - 1
        right_idx = idx + 1
        left: Number = self.calculation_state[left_idx]
        right: Number = self.calculation_state[right_idx]
        result = action.get_action()(left.value, right.value)
        print('result', result)
        self.update_current_state(result, left_idx, right_idx)

    def update_current_state(self, result: float, left: int, right: int):
        new_state = []

        if (left) > 0:
            u = self.calculation_state[0:(left)]
            new_state.extend(u)

        new_state.append(Number(result))

        if right + 1 <= len(self.calculation_state):
            new_state.extend(self.calculation_state[(right + 1)::])

        self.calculation_state = new_state
        print('new_state', new_state)
        del new_state


if __name__ == '__main__':
    # expression = '10 + 2 / ( 4 - 1) + 5'
    expression = '10 + 2 * 3 / 2'

    c = Calculator(expression).run()
    print(c)
