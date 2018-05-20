from xml.etree import cElementTree as ElementTree

from src import XmlDictConfig


def test():

    tree = ElementTree.parse('wellspring87808,999,744 O15-04-06.xml')
    root = tree.getroot()
    xmldict = XmlDictConfig(root)


test()