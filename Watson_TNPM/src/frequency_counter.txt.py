from collections import Counter
import csv
import requests
import xml.etree.ElementTree as ET
import os

def parse_finalXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    comment=''
    for subelement in root:
        if subelement.tag == 'COMMENT':
            comment= subelement.text
    # create empty list for news items
    PMRs = []
    str1=''
    str_final=''
    for item in root.findall('./text'):
            news = {}
            for child in item:
                print(child.text)
                childlines = child.text.split(os.linesep)
            for line in childlines:
                print(line)

parse_finalXML('wellspring14864,122,000 O16-01-12.xml')
