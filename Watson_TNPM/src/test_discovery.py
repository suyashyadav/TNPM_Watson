import json
import wx
import configparser
import requests
from watson_developer_cloud import NaturalLanguageClassifierV1
from watson_developer_cloud import DiscoveryV1
import Collection_Query
import progressbar


config = configparser.RawConfigParser()
config.read('configfile.properties')
collection_id = config.get('DISCOVERY_SECTION','Test_Collection_id')
natural_language_classifier_1 = NaturalLanguageClassifierV1(
  username=config.get('NLCSECTION','username'),
  password=config.get('NLCSECTION','password'))
discovery = DiscoveryV1(
  username="81857d90-6cce-47fc-997c-c7b26f1a0084",
  password="8e8niHrxidKH",
  version="2017-08-01"
)
Solution_list=[]
Document_list= set()
passage_filename = {}


def get_Document_Suggestion(query_input,Filter):
    qopts = {'query': query_input, 'filter': 'text:' + Filter, 'passages': 'true'}
    query_response = discovery.query(config.get('DISCOVERY_SECTION', 'Environment_id'), collection_id, qopts)
    #if not query_response["passages"]:
        #for response in query_response["results"]:
           # if response["score"] > .2:
            #    Document_list.add(response["extracted_metadata"]["title"])
       # print(Document_list)
    #else:
    #print("passage retrieval successful")
    for response in query_response["passages"]:
            if response["passage_score"] > 18:
                doc_info = discovery.get_document('fc80f619-8cfd-4131-962a-c6dd8944bbae',
                                                  '9ca1a3fa-a90a-4e3c-ba84-1e1053bfbc75',
                                                  response["document_id"])
                passage_filename[doc_info["filename"]]=response["passage_text"]
    #print(doc_info["filename"])
    #print(response["passage_text"])
    #print(passage_filename)
    #print(response)
    #print(doc_info)

                # Document_list.add(response["extracted_metadata"]["title"])
                # print(response["extracted_metadata"]["title"])
                # print(json.dumps(response,indent=2))
                # print(response["text"])
                # print(Document_list)
                # Collection_Query.Query_Collection(query_input, Document_list)
    return passage_filename;
#get_Document_Suggestion("Missing NRAW data","Datachannel")