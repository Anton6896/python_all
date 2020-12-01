import xml.sax
import pathlib
import os
# file based structured data (xml, json etc)

os.chdir(pathlib.Path(
    __file__).parent.absolute())

xml_file: str = str(pathlib.Path(
    __file__).parent.absolute()) + "/filename.xml"






if __name__ == "__main__":
    print(xml_file)