import xml.etree.ElementTree as ET
from collections import defaultdict
import csv
from os import path
import re


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    # create empty list for news items
    comment = ''
    for subelement in root:
        if subelement.tag == 'COMMENT':
            comment = subelement.text
    Actions = []
    str1=''
    str_final=''
    splitstr=''
    count=False
    for item in root.findall('./text'):
            for child in item:
                if "Action taken" in child.text:
                    count=True
                    str_final = str_final + child.text
                elif "ACTION TAKEN" in child.text:
                    count=True
                    str_final = str_final + child.text
                elif "Action plan" in child.text:
                    count=False
                    Actions.append(str_final)
                    str_final=''
                elif "ACTION PLAN"  in child.text:
                    count=False
                    Actions.append(str_final)
                    str_final = ''
                elif count:
                    str_final=str_final+child.text
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "testing.csv"))
    for Action in Actions[:]:
        with open(filepath, 'a', newline='') as training_data:
            writer = csv.writer(training_data)
            writer.writerow([comment, re.sub('\s+', ' ', Action.replace('\n', ' ').replace('\r', '')).strip()])



def savetoCSV(PMRs, filename):
    # specifying the fields for csv file
    fields = ['line']

    # writing to csv file
    with open(filename, 'w',encoding='utf8',newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(PMRs)

def main():

    PMRs = parseXML('wellspring00054,082,000 O15-11-25.xml')
    #savetoCSV(PMRs, 'Wellspring00377,999,805 O15-03-09.csv')

if __name__ == "__main__":
    # calling main function
    main()