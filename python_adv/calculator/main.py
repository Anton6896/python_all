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
        }.get(self.value) or add

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
                        self.tokens.append(
                            Token(type_of=Token.NUMBER, value=float(holder.strip())))
                except ValueError:
                    raise Exception(
                        'its not math expression: ' + self.expression)

                self.tokens.append(Token(type_of=Token.ACTION, value=ch))
                holder = ''
            else:
                holder += ch

        if holder.strip():
            self.tokens.append(
                Token(type_of=Token.NUMBER, value=float(holder.strip())))


class Node:
    def __init__(self, token: Token):
        self.token = token
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.height = 1
        self.value = None

    def __str__(self):
        if self.token:
            return f'{self.token.value}({self.weight})'
        return ''

    def __repr__(self):
        if self.token:
            return f'<Node> {self.token.value}[{self.weight}]'
        return ''

    def calculate(self):
        if self.token.type_of != Token.ACTION:
            return

        if (
                self.left.value and self.right.value
        ):
            self.value = self.token.use_it()(self.left.value, self.right.value)

        elif (
                self.left.value and self.right.token.type_of == Token.NUMBER
        ):
            self.value = self.token.use_it()(self.left.value, self.right.token.value)

        elif (
                self.left.token.type_of == Token.NUMBER and self.right.value
        ):
            self.value = self.token.use_it()(self.left.token.value, self.right.value)

        elif (
                self.left.token.type_of == Token.NUMBER and self.right.token.type_of == Token.NUMBER
        ):
            self.value = self.token.use_it()(self.left.token.value, self.right.token.value)

        # elif (
        #     self.left.token.type_of == Token.ACTION
        # ):
        #     self.left.value = self.left.calculate()
        return self.value

    @property
    def weight(self):
        """
        numbers:        3
        actions: *|/    2
        actions: +|-    1
        """
        if self.token.type_of == Token.NUMBER:
            return 3
        return 2 if self.token.is_priority_action else 1


class Tree:
    def __init__(self):
        self.root: Node | None = None
        self.response = []

    def push(self, new_node: Node):
        if not self.root:
            logger.info('%s pushing to root', new_node)
            self.root = new_node
            return self

        current_node: Node = self.get_most_right(self.root)
        self._push(current_node, new_node)

    """
    this logic not working ! 
    will not compare weight. now will check instance type 
    """

    def _push(self, current_node: Node, new_node: Node):
        # working with root
        if all([
            not current_node.parent,
            not current_node.left
        ]):
            logger.info('new root %s, left %s', new_node, current_node)
            current_node.parent = new_node
            new_node.left = current_node
            self.root = new_node
            return self

        if all([
            not current_node.parent,
            current_node.left,
            not current_node.right
        ]):
            logger.info('%s pushing to right', new_node)
            new_node.left = current_node.right
            current_node.right = new_node
            new_node.parent = current_node
            return self

        # other movements
        if current_node.weight > new_node.weight:
            self.lighter_weight(current_node, new_node)
        elif current_node.weight < new_node.weight:
            self.heavier_weight(current_node, new_node)
        else:
            self.same_weight(current_node, new_node)

    def lighter_weight(self, current_node: Node, new_node: Node):
        logger.info('new node %s is lighter then %s', new_node, current_node)

        if not current_node.parent:
            logger.info('new root %s, left %s', new_node, current_node)
            new_node.left = current_node
            current_node.parent = new_node
            self.root = new_node
            return self

        self._push(current_node.parent, new_node)

    def heavier_weight(self, current_node: Node, new_node: Node):
        logger.info('new node %s is havier then %s', new_node, current_node)
        if (
                current_node.left
                and not current_node.right
        ):
            current_node.right = new_node
            new_node.parent = current_node
            return self

        # * | /
        if current_node.weight < new_node.weight < current_node.right.weight:
            new_node.left = current_node
            new_node.parent = current_node.parent
            new_node.parent.right = new_node
            current_node.parent = new_node

    def same_weight(self, current_node: Node, new_node: Node):
        logger.info(f'current %s same weight then new node %s', current_node, new_node)
        # if not current_node.left:
        #     raise RuntimeError('invalid operations (++, -- ...)')

        if not current_node.parent:
            self.root = new_node
        else:
            new_node.parent = current_node.parent

        new_node.left = current_node
        current_node.parent = new_node

        return self

    def calculate_self(self, node: Node | None, res=None) -> float | list:
        print(node.left, node, node.right)
        if not node or node.token.type_of != Token.ACTION:
            return []

        if node.right:
            res.extend(self.calculate_self(node.right, res))
        if node.left:
            res.extend(self.calculate_self(node.left, res))

        node.calculate()
        res.append(node.calculate())

        return res

    def get_most_right(self, node: Node) -> Node:
        if node.right:
            return self.get_most_right(node.right)
        return node

    def in_order(self, node: Node = None) -> list:
        # Left -> Root -> Right
        res = []
        if node:
            res.extend(self.in_order(node.left))
            res.append(node.token.value)
            res.extend(self.in_order(node.right))
        return res

    def __repr__(self) -> str:
        return f'<Tree> {self.in_order(self.root)}'


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
                    if token.is_end_parenthesis:
                        inner_result = inner_tree.calculate_self(inner_tree.root)
                        main_tree.push(Node(token=Token(type_of=Token.NUMBER, value=inner_result)))
                        break
                    inner_tree.push(Node(token=token))

            main_tree.push(Node(token=token))

        logger.info('inorder %s', main_tree)
        res = []
        return main_tree.calculate_self(main_tree.root, res)


if __name__ == '__main__':
    result = Worker('2 + 3 - 1 + 1 + 4 -2').run()
    logger.info('result: %s', result)
