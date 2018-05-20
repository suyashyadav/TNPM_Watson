import json
from watson_developer_cloud import NaturalLanguageClassifierV1
from os import path

natural_language_classifier_1 = NaturalLanguageClassifierV1(
  username='5d62674d-c329-4ad8-9a19-01004dad9669',
  password='o4QEuegIBdke')


def create_Classifier():
  #classifier_ids = []
  #classifiers = natural_language_classifier_1.list()
  #for classifier in classifiers["classifiers"]:
   # classifier_ids.append(classifier["classifier_id"])
  #natural_language_classifier_1.remove(classifier_ids[0])
  #with open('D:/Watson/WATSON_TRAINING_DATA/training_data_Wireline_Latest_new.csv', 'rb') as training_data:
  basepath = path.dirname(__file__)
  filepath = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "Wireline_training_data.csv"))
  with open(filepath, "rb") as training_data:
    new_classifier =  natural_language_classifier_1.create(
    training_data=training_data,
    name='Natural Language Classifier_test',
    language='en'
  )
  #return  new_classifier

create_Classifier();
#print(json.dumps(classifier, indent=2))