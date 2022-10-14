from curses.ascii import isdigit
from enum import Enum


class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        L_PAREN = 3
        R_PAREN = 4
        SPACE = 5

    def __init__(self, type: Type, text: str) -> None:
        self.type = type
        self.text = text

    def __str__(self) -> str:
        return f'{self.text}'


def lex(input: str) -> list[Token]:
    # (1+2) - 3 check this kind of expressions

    acc: list[Token] = []
    i = 0

    while i < len(input):
        if input[i] == '+':
            acc.append(Token(Token.Type.PLUS, input[i]))
        elif input[i] == '-':
            acc.append(Token(Token.Type.MINUS, input[i]))
        elif input[i] == ')':
            acc.append(Token(Token.Type.R_PAREN, input[i]))
        elif input[i] == '(':
            acc.append(Token(Token.Type.L_PAREN, input[i]))
        elif input[i] == ' ':
            acc.append(Token(Token.Type.SPACE, input[i]))

        # check numbers
        else:
            digits = [input[i], ]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    break
            acc.append(Token(Token.Type.INTEGER, ''.join(digits)))

        i += 1

    return acc


def calc(input):
    tokens = lex(input)
    print(''.join(map(str, tokens)))


if __name__ == '__main__':
    exp = '(1+2) - 3'
    calc(exp)
