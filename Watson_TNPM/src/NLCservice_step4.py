import json
import wx
import configparser
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
#Solution_list=[]
Document_list= set()


def get_Document_Suggestion(query_input,Filter):
    qopts = {'query': query_input, 'filter': 'text:'+Filter}
    query_response = discovery.query(config.get('DISCOVERY_SECTION', 'Environment_id'), collection_id, qopts)
    for response in query_response["results"]:
        if response["score"] > .2:
            Document_list.add(response["extracted_metadata"]["title"])
            #print(response["extracted_metadata"]["title"])
            #print(json.dumps(response,indent=2))
            #print(response["text"])
    return Document_list
    #Collection_Query.Query_Collection(query_input, Document_list)


def classify_problem(query_input):
  #print("inside classify problem"+query_input)
  n = 0;
  Solution_list = []
  classifier_ids = []
  classifiers = natural_language_classifier_1.list()
  for classifier in classifiers["classifiers"]:
      classifier_ids.append(classifier["classifier_id"])
  config.set('NLCSECTION', 'classifier_id', classifier_ids[0])
  #print(classifier_ids[0])
  with open('configfile.properties', 'w') as configfile:
      config.write(configfile)
  status = natural_language_classifier_1.status(config.get('NLCSECTION', 'classifier_id'))
  #print(status)
  if status["status"] != 'Available':
      Solution_list.append("Status Unavailable")
      return Solution_list
  else:
        classes = natural_language_classifier_1.classify(config.get('NLCSECTION','classifier_id'),query_input)
  #classes_complete = natural_language_classifier_1.classify(config.get('NLCSECTION','classifier_id'),query_input)
  #print(config.get('NLCSECTION','classifier_id'))

  #bar = progressbar.ProgressBar(max_value=100)
  #print(json.dumps(classes,indent=2))
  #for n in classes:
  #print(classes["classes"][0]["confidence"])
  #print(len(classes["classes"]))
  #bar.start()
  #print("*********************************************************************************************")
  #print("****************************WATSON CLASSIFIER FOR TNPM *******************************")

        for classes in classes["classes"]:
            if classes["confidence"] > .1:
         #print("Top Suggestion for the problem description entered is : ")
         #Collection_Query.Query_Classifier(query_input, classes["class_name"])
                Solution_list.append(classes["class_name"])
                n = n=+1
        if n == 0:
                Solution_list.append("No output")
                return  Solution_list
        else:
              #Collection_Query.Query_Classifier(query_input, Solution_list)
                return Solution_list














