import json
from watson_developer_cloud import NaturalLanguageClassifierV1
from os import path

natural_language_classifier_1 = NaturalLanguageClassifierV1(
  #username='ac6c5d42-b620-40af-95c3-24d5302a63cb',
 #password='jV8aqdLFFKoU'

  username='5d62674d-c329-4ad8-9a19-01004dad9669',
  password='o4QEuegIBdke'

)

def create_Classifier_new():
  # with open('D:/Watson/WATSON_TRAINING_DATA/training_data_Wireline_Latest_new.csv', 'rb') as training_data:
  basepath = path.dirname(__file__)
  filepath = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "Clean_Wireline_training_data.csv"))
  with open(filepath, "rb") as training_data:
    classifier =  natural_language_classifier_1.create(
    training_data=training_data,
    name='Natural Language Classifier_test',
    #name='Natural Language Classifier_test',
    language='en'
  )
  print(json.dumps(classifier, indent=2))

create_Classifier_new()
