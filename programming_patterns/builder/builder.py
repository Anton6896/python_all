"""
builder pattern 
create an convenient way for creating conplicated objects 
"""


def func_1():
    # html constraction
    words = ['hello', 'world ']
    parts = ['<ul>']

    for w in words:
        parts.append(f'    <li>{w}</li>')
    parts.append('</li>')
    print('\n'.join(parts))


class HtmlElement:
    # create html element (recursively)
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = " " * ((indent+1) * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " "*((indent+1)*self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent+1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    pass


if __name__ == "__main__":
    func_1()
