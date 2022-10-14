from enum import Enum


class Token:
    class Type(Enum):
        INTEGER = 0
        PLUS = 1
        MINUS = 2
        L_PAREN = 3
        R_PAREN = 4
    
    def __init__(self, type: Type, text: str) -> None:
        self.type = type
        self.text = text
    
    def __str__(self) -> str:
        return f'`{self.text}`'


def lex(input):
    acc = []

    