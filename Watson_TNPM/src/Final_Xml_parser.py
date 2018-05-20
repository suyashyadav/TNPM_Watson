# Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
import os
import urllib
import csv
from os import path
import re

username = "1suyash@my.ibm.com"
password = "ilusssm@1323"
def loadUrl():
    # url of rss feed
    #url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
    url = 'https://etest.lenexa.ibm.com:9445/WellspringDataAPI/recordsAuth?method=query&source=PMR&compids=5725C1500&firstmoddate=2016-01-01&lastmoddate=2016-06-30'
    resp = requests.get(url,auth=(username,password),verify=False)

    # saving the xml file
    with open('Wellspring.xml', 'wb') as f:
        f.write(resp.content)


def parseXML(xmlfile):
    # create element tree object
    tree = ET.parse(xmlfile)
    # get root element
    root = tree.getroot()
    # create empty list for news items
    PMRs = []
    for item in root.findall('./result'):

            # empty news dictionary
            news = {}
            #iterate child elements of item
            for child in item:
                # special checking for namespace object content:media
                    news[child.tag] = child.text

            # append news dictionary to news items list
            PMRs.append(news)

    return PMRs

def parse_finalXML(PMR_no,xmlfile):
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
    filepath = path.abspath(path.join(basepath, "..", "../Watson_Training_Datacap", "testing.csv"))
    for Action in Actions[-3:]:
        with open(filepath, 'a', newline='') as training_data:
            writer = csv.writer(training_data)
            writer.writerow([comment, PMR_no+" "+re.sub('\s+', ' ', Action.replace('\n', ' ').replace('\r', '')).strip()])

def savetoCSV(PMRs, filename):
    # specifying the fields for csv file
    fields = ['src', 'id', 'date']

    # writing to csv file
    with open(filename, 'w',encoding='utf8',newline='') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(PMRs)

def fetchPMR(filename):
     with open(filename,'r') as csvfile:
        next(csvfile)
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
           # print(row[1]+","+row[2]+","+row[3])
           # strnew = (row[1:4])
            completeUrl=buildUrl(row[1])
            PMR_no=row[1].replace("/","-")
            #print(completeUrl)
            completeUrl=completeUrl.replace(" ", "%20")
            #completeUrl=urllib.parse.quote(completeUrl)
            print(completeUrl)
            response=requests.get(completeUrl, auth=(username, password), verify=False)
            filename='wellspring'+PMR_no+'.xml'
            with open(filename, 'wb') as f:
                f.write(response.content)
            parse_finalXML(PMR_no,filename)



def buildUrl(id):
    url_new = "https://etest.lenexa.ibm.com:9445/WellspringDataAPI/recordsAuth?method=fetch&source=PMR&"
    id=id
    retfields = "pmrno,bno,cno,create_date,comment,status,text"
    completeUrl=url_new+"id="+id+"&retfields="+retfields
    return completeUrl




def main():
    # load URLs to update existing xml file
    loadUrl()

    # parse xml file
    PMRs = parseXML('Wellspring.xml')

    # store PMRs  in a csv file
    savetoCSV(PMRs, 'Wellspring.csv')
    fetchPMR('Wellspring.csv')


if __name__ == "__main__":
    # calling main function
    main()