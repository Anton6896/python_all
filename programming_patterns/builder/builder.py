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

        i = " " * ((indent+1) * self.indent_size)  # i = 4 -> "    "
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " "*((indent+2)*self.indent_size)  # i1 = 8 -> "    "
            lines.append(f"{i1}{self.text}")

        # recursion call for all elements from HtmlBuilder
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
    __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    # not fluent implementation
    def add_child(self, ch_name, ch_text):
        self.__root.elements.append(
            HtmlElement(ch_name, ch_text)
        )

    # fluent implementation
    def add_child_fluent(self, ch_name, ch_text):
        self.__root.elements.append(
            HtmlElement(ch_name, ch_text)
        )
        return self

    def __str__(self):
        return str(self.__root)

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)


if __name__ == "__main__":
    # func_1()

    # ordinary call
    builder = HtmlBuilder('ul')
    # builder = HtmlElement.create('ul')
    builder.add_child('li', 'text 1')
    builder.add_child('li', 'text 2')

    print(f'ordinary builder \n{builder}')

    # fluent call
    print()
    builder.clear()   # first initialized name "<ul>"
    builder.add_child_fluent('li', 'hello') \
        .add_child_fluent('li', 'world')

    print('Fluent builder:')
    print(builder)
