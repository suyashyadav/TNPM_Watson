import xml.etree.ElementTree as ET
from collections import defaultdict
import csv


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    # create empty list for news items
    PMRs = []

    for item in root.findall('./text'):
            news = defaultdict(list)
            for child in item:
                    news[child.tag].append(child.text)
            PMRs.append(news)
    print(PMRs)

    return PMRs


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

    PMRs = parseXML('wellspring00377,999,805 O15-03-09.xml')
    savetoCSV(PMRs, 'Wellspring00377,999,805 O15-03-09.csv')

if __name__ == "__main__":
    # calling main function
    main()