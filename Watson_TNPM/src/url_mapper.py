import json
import wx
import configparser
from watson_developer_cloud import NaturalLanguageClassifierV1
from watson_developer_cloud import DiscoveryV1
import Collection_Query
import progressbar


config = configparser.RawConfigParser()
config.read('configfile.properties')
natural_language_classifier_1 = NaturalLanguageClassifierV1(
  username=config.get('URL_MAPPING_SECTION','username'),
  password=config.get('URL_MAPPING_SECTION','password'))
Solution_list=[]
Document_list= set()
suggestion_dict= {}

def classify_problem(documents):
  for document in documents:
    #print("inside classify problem"+document)
    n = 0;
    print(document)
    classes = natural_language_classifier_1.classify(config.get('URL_MAPPING_SECTION','classifier_id'),document)
    print(classes)
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
        if classes["confidence"] > .9:
            #print("Top Suggestion for the problem description entered is : ")
            #Collection_Query.Query_Classifier(query_input, classes["class_name"])
            Solution_list.append(classes["class_name"])
            #print(classes["class_name"])
            n =+ 1

    if n == 0:
         print("sorry, we didn't find any match")
  #else:
      #Collection_Query.Query_Classifier(query_input, Solution_list)
      #return Solution_list
    elif n == 1:
        for solution in Solution_list:
            solution_string = solution
            suggestion_dict[document] = solution_string

    else:
        print("sorry we found more then one urls")

  return suggestion_dict