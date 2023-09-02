import logging

from dataclasses import dataclass
from operator import add
from operator import floordiv
from operator import mul
from operator import sub

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class Token:
    ACTION = 'action'
    NUMBER = 'number'

    type_of: str
    value: str | float

    def use_it(self):
        return {
            '+': add,
            '-': sub,
            '*': mul,
            '/': floordiv,
        }.get(self.type_of) or add

    @staticmethod
    def get_available_actions():
        return '+', '-', '*', '/', '(', ')'

    @property
    def is_start_parenthesis(self):
        return self.type_of == self.ACTION and self.value == '('

    @property
    def is_end_parenthesis(self):
        return self.type_of == self.ACTION and self.value == ')'

    @property
    def is_priority_action(self) -> bool:
        return self.type_of == self.ACTION and self.value in ('*', '/')


class Tokenizer:
    def __init__(self, expression: str):
        self.expression = expression
        self.tokens = []

    def run(self):
        try:
            self._run()
            return self.tokens
        except Exception as e:  # noqa
            logger.exception(str(e))

    def _run(self):
        logger.info('tokenizing ...')
        holder = ''
        for ch in self.expression:
            if ch in Token.get_available_actions():
                try:
                    if holder.strip():
                        self.tokens.append(Token(type_of=Token.NUMBER, value=float(holder.strip())))
                except ValueError:
                    raise Exception('its not math expression: ' + self.expression)

                self.tokens.append(Token(type_of=Token.ACTION, value=ch))
                holder = ''
            else:
                holder += ch

        if holder.strip():
            self.tokens.append(Token(type_of=Token.NUMBER, value=float(holder.strip())))


class Node:
    def __init__(self, token: Token):
        self.token = token
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

    @property
    def weight(self):
        if self.token.type_of == Token.NUMBER:
            return 3

        return 2 if self.token.is_priority_action else 1


class Tree:
    def __init__(self):
        self.root: Node = None

    def push(self, new_node: Node):
        if not self.root:
            self.root = new_node
            return self

        # if self.root and not self.root.left:
        #     self.root.left = new_node
        #     new_node.parent = self.root
        #
        #
        # elif self.root and not self.root.right:
        #     ...

        current_node: Node = self.get_next_target(self.root)

        if current_node.weight > new_node.weight:
            self.new_lightweight(current_node, new_node)

        elif current_node.weight < new_node.weight:
            ...

        else:
            ...

    def new_lightweight(self, target_node: Node, new_node: Node):
        # handle initial inputs
        # is root
        if not target_node.parent and not target_node.left:
            target_node.parent = new_node
            new_node.left = target_node
            self.root = new_node

        elif not target_node.parent and not target_node.right:
            new_node.parent = self.root
            self.root.right = new_node

    def calculate_self(self) -> float:
        ...

    def get_next_target(self, node: Node) -> Node:
        """
        getting most right node
        """
        if node.right:
            return self.get_next_target(node.right)
        return node


class Worker:
    def __init__(self, expression: str):
        self.expression = expression
        self.token_data = None

    def run(self) -> float | str:
        self.token_data = Tokenizer(self.expression).run()
        main_result = self.use_tree()
        return main_result or self.expression

    def use_tree(self) -> float | None:
        main_tree = Tree()

        while self.token_data:
            token: Token = self.token_data.pop(0)

            # handle parenthesis
            if token.is_start_parenthesis:
                inner_tree = Tree()
                while self.token_data:
                    token: Token = self.token_data.pop(0)
                    inner_tree.push(Node(token=token))
                    if token.is_end_parenthesis:
                        inner_result = inner_tree.calculate_self()
                        main_tree.push(Node(Token(type_of=Token.NUMBER, value=inner_result)))
                        break

            main_tree.push(Node(token=token))

        return main_tree.calculate_self()


if __name__ == '__main__':
    result = Worker('1 + 2').run()
    print(result)
