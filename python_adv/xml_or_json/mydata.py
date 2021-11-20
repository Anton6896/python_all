import xml.sax
import xml.dom.minidom
import pathlib
import os
# file based structured data (xml, json etc)


os.chdir(pathlib.Path(
    __file__).parent.absolute())

xml_file: str = str(pathlib.Path(
    __file__).parent.absolute()) + "/person.xml"


class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("----person :")
            print("id: {}".format(attrs["id"]))

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content

    def endElement(self, name):
        if self.current == "name":
            print(f"name {self.name}")
        elif self.current == "age":
            print(f"age {self.age}")
        elif self.current == "weight":
            print(f"weight {self.weight}")
        self.current = ""


def hand():
    handler = GroupHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)


def ff():
    from xml.dom import minidom

    # parse an xml file by name
    mydoc = minidom.parse('person.xml')

    items = mydoc.getElementsByTagName('person')

    # total amount of items
    print(len(items))


def dom():
    # https://www.youtube.com/watch?v=R2bhO0kZZnQ&list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1&index=10&ab_channel=NeuralNine
    pass


if __name__ == "__main__":
    # hand()
    dom()
