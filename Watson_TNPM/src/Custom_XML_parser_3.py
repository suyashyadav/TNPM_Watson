import os
from xml.etree import ElementTree as ET





def main():
    rootElement = ET.parse("wellspring87808,999,744 O15-04-06.xml").getroot()

    for subelement in rootElement:
        print  ("Tag: ", subelement.tag)
        print   ( "Text: ", subelement.text)



if __name__ == "__main__":
    main()
