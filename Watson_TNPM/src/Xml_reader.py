# Python code to illustrate parsing of XML files
# importing the required modules
import csv
import requests
import xml.etree.ElementTree as ET
import os
import urllib

username = "1suyash@my.ibm.com"
password = "ilusssm@1323"
def loadUrl():
    # url of rss feed
    #url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
    url = 'https://etest.lenexa.ibm.com:9445/WellspringDataAPI/recordsAuth?method=query&source=PMR&compids=5725C1501&firstmoddate=2016-01-20&lastmoddate=2016-01-21'
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
    count=0
    for item in root.findall('./text'):
            news = {}
            for child in item:
                if "ACTION TAKEN:" in child.text:
                    str1 = ''
                elif "Action Taken:" in child.text:
                    str1 = ''
                elif "ACTION PLAN:" in child.text:
                    str_final = str1
                elif "Action Plan:" in child.text:
                    str_final = str1
                else:
                    str1 = str1 + child.text
            print(comment+":"+str_final)
            print("======================")
                #news[child.attrib['num']] = child.text

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
            parse_finalXML(filename)



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