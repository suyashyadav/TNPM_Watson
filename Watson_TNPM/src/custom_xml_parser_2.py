#!/usr/bin/python

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.security = ""
        self.PMRNO = ""
        self.BNO = ""
        self.CNO = ""
        self.CREATE_DATE = ""
        self.COMMENT = ""
        self.STATUS = ""
        self.text = ""
    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "line":
            print("*****text*****")


    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "security":
            print( "security:", self.security)
        elif self.CurrentData == "PMRNO":
            print( "PMRNO:", self.PMRNO)
        elif self.CurrentData == "BNO":
            print( "BNO:", self.BNO)
        elif self.CurrentData == "CNO":
            print( "CNO:", self.CNO)
        elif self.CurrentData == "CREATE_DATE":
            print ("CREATE_DATE:", self.CREATE_DATE)
        elif self.CurrentData == "COMMENT":
            print ( "COMMENT:", self.COMMENT)
        elif self.CurrentData == "STATUS":
            print("STATUS:", self.STATUS)
        elif self.CurrentData == "text":
            print("text:", self.text)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "security":
            self.security = content
        elif self.CurrentData == "PMRNO":
            self.PMRNO = content
        elif self.CurrentData == "BNO":
            self.BNO = content
        elif self.CurrentData == "CNO":
            self.CNO = content
        elif self.CurrentData == "CREATE_DATE":
            self.CREATE_DATE = content
        elif self.CurrentData == "COMMENT":
            self.COMMENT = content
        elif self.CurrentData == "STATUS":
            self.STATUS = content
        elif self.CurrentData == "text":
            self.text = content

if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("wellspring00377,999,805 O15-03-09.xml")