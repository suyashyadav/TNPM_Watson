import sys
import os
import json
import wx
import configparser
import csv
from watson_developer_cloud import DiscoveryV1
import NLCservice
import NLCservice_step4


config = configparser.RawConfigParser()
config.read('configfile.properties')
discovery = DiscoveryV1(
  username="81857d90-6cce-47fc-997c-c7b26f1a0084",
  password="8e8niHrxidKH",
  version="2017-08-01"
)

def Query_Classifier(query,top_classes):
  Frame_2 = wx.Frame(None, title='Classifier_Output',
                     style=wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                     size=wx.Size(550, 750))
  font1 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'MS Sans Series')
  Frame_2.SetFont(font1)
  panel = wx.Panel(Frame_2)
  Filters = query.split()
  font1 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'MS Sans Series')
  label = wx.StaticText(panel, label="Top Suggestion for the problem description entered is :",pos=(5,5))
  result_Yes = wx.StaticText(panel, label="", pos=(5, 420))
  result_Yes.Hide()
  result_No = wx.StaticText(panel, label="", pos=(10, 420))
  result_No.Hide()
  combo = wx.ComboBox(panel, wx.CB_DROPDOWN, pos=(240, 575),size=wx.Size(250,50),style=wx.TE_PROCESS_ENTER,choices=Filters)
  combo.Hide()
  Enter_Suggestion = wx.StaticText(panel, label="", pos=(10, 420))
  label.SetFont(font1)
  Label_Suggestion = wx.StaticText(panel, label="", pos=(10, 490))
  Label_Document_Search=wx.StaticText(panel, label="Thanks, Do you want to look for relevant documents to get more information", pos=(10, 510))
  Label_Document_Search.Hide()
  Button_Suggestion = wx.Button(panel, pos=(10, 590), label="Use My Suggestion")
  Button_Suggestion.Hide()
  #TextArea= wx.TextCtrl(panel,style=wx.TE_MULTILINE,size=wx.Size(550,600))
  TextArea = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(10, 30), size=(520, 300))
  TextArea_2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(10, 510), size=(520, 70))
  TextArea_2.Hide();
  for classes in top_classes:
    TextArea.AppendText("\n=============================================================\n")
    TextArea.AppendText(classes)
    TextArea.AppendText("\n=============================================================\n")
  TextArea.SetFont(font1)


  label_2 = wx.StaticText(panel, label="Do you feel the above suggestion is useful:",pos=(10,350))
  #result = wx.StaticText(panel, label="",pos=(225,450))



  def onYesButton(self):
    Enter_Suggestion.SetLabel("Thanks,Do you want to enter your suggestion for this issue to help improve the relevancy")
    Button_improve_relevency.Show()
    Button_do_not_improve_relevency.Show()



  def onNoButton(self):
    Enter_Suggestion.SetLabel("Thanks,Do you want to enter your suggestion for this issue to help improve the relevancy")
    Button_improve_relevency.Show()
    Button_do_not_improve_relevency.Show()



  def onSuggestionButton(self):
    classifier_ids=[]
    suggestion = TextArea_2.GetValue()
    TextArea_2.Hide()
    Button_Yes.Hide()
    Button_No.Hide()
    Button_do_not_improve_relevency.Hide()
    Button_improve_relevency.Hide()
    result_Yes.Hide()
    result_No.Hide()
    label_2.Hide()
    Label_Suggestion.Hide()
    Enter_Suggestion.Hide()
    Button_Suggestion.Hide()
    with open('D:/Watson/WATSON_TRAINING_DATA_18thSep/training_data_Wireline_TP_Latest.csv', 'a', newline='') as training_data:
      writer=csv.writer(training_data)
      writer.writerow([query,suggestion])
      New_classfier=NLCservice.create_Classifier()
      label_confirmation=wx.StaticText(panel, label="Your Suggestion has been appended to training data and submitted to classifier", pos=(10, 410))
      label_confirmation.SetFont(font1)
      label_new_classifier_id=wx.StaticText(panel, label="New_Classifier id " + New_classfier["classifier_id"] , pos=(10, 430))
      label_new_classifier_id.SetFont(font1)
      label_new_classifier_status=wx.StaticText(panel, label=New_classfier["status_description"], pos=(10, 450))
      label_new_classifier_status.SetFont(font1)
      Label_Document_Search.Show()
      Button_Yes_More_Info.Show()
      Button_No_More_Info.Show()
      #result.SetLabel("Thanks, Do you also want to look for relevant documents to get more information")


  def onYesMoreInfoButton(self):
     label_filter=wx.StaticText(panel,label="Please enter or select appropriate filter", pos=(10,580))
     combo.Show()
     Button_Send_to_Discovery=wx.Button(panel, pos=(120,620),label="Send to Discovery")
     Button_Send_to_Discovery.Bind(wx.EVT_BUTTON,sendToDiscovery)

  def  sendToDiscovery(self):
    NLCservice_step4.get_Document_Suggestion(query,combo.GetValue())
    Frame_2.Close()

  def onNoMoreInfoButton(self):
     label_Final_Thanks=wx.StaticText(panel,label="Thanks,it was nice working with you", pos=(120,570))
     label_Final_Thanks.SetFont(font1)

  def onImproveRelevancy(self):
    Label_Suggestion.SetLabel("Please enter your Suggestion Below for this problem Description")
    TextArea_2.Show()
    Button_Suggestion.Show()
    Button_Suggestion.Bind(wx.EVT_BUTTON, onSuggestionButton)

  def onDo_NotImproveRelevancy(self):
    Label_Document_Search.Show()
    Button_Yes_More_Info.Show()
    Button_No_More_Info.Show()


#Below commented lines are just for removeing the classifier as we have limitation on the number of classifier.
      #classifiers=NLCservice_step2.list_Classifer()
     # for classfier in classifiers["classifiers"]:
       # classifier_ids.append(classfier["classifier_id"])
      #Remove_Classifier.remove_classifier(classifier_ids[0])




  Button_Yes = wx.Button(panel,pos=(10, 380), label="Yes")
  Button_Yes.Bind(wx.EVT_BUTTON,onYesButton)
  Button_No = wx.Button(panel, pos=(400, 380), label="No")
  Button_No.Bind(wx.EVT_BUTTON,onNoButton)
  Button_Yes_More_Info= wx.Button(panel,pos=(10, 540), label="Yes")
  Button_Yes_More_Info.Bind(wx.EVT_BUTTON,onYesMoreInfoButton)
  Button_Yes_More_Info.Hide()
  Button_No_More_Info = wx.Button(panel, pos=(400, 540), label="No")
  Button_No_More_Info.Bind(wx.EVT_BUTTON,onNoMoreInfoButton)
  Button_No_More_Info.Hide()
  Button_improve_relevency=wx.Button(panel,pos=(10,460),label="Yes")
  Button_improve_relevency.Bind(wx.EVT_BUTTON,onImproveRelevancy)
  Button_improve_relevency.Hide()
  Button_do_not_improve_relevency = wx.Button(panel, pos=(400, 460),label="No")
  Button_do_not_improve_relevency.Bind(wx.EVT_BUTTON,onDo_NotImproveRelevancy)
  Button_do_not_improve_relevency.Hide()


  Frame_2.Show()


  #print(query,"    ",top_class)
  #print(config.get('DISCOVERY_SECTION','Environment_id'),config.get('DISCOVERY_SECTION',collection+'_id'))
  #qopts = {'query': 'enriched_text.keywords.text:Netcool Performance Manager', 'filter': 'enriched_text.concepts.text::IBM'}
  #qopts = {'query': query, 'filter': 'text:DataView'}
 # my_query = discovery.query(config.get('DISCOVERY_SECTION','Environment_id'),config.get('DISCOVERY_SECTION',collection+'_id'), qopts)
  #print(json.dumps(my_query, indent=2))


def Query_Collection(query,Documents):
  Frame_3 = wx.Frame(None, title='Discovery_Service_Output',
                     style=wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                     size=wx.Size(550, 650))
  font1 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'MS Sans Series')
  Frame_3.SetFont(font1)
  panel = wx.Panel(Frame_3)
  font1 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'MS Sans Series')
  label = wx.StaticText(panel, label="Top Documents suggestion for the problem description entered is :", pos=(5, 5))
  label.SetFont(font1)
  Label_Suggestion_discovery=wx.StaticText(panel,label="Please enter relevant documents to Improve the relevancy",pos=(10,440))
  Label_Suggestion_discovery.Hide()
  font1 = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'MS Sans Series')
  TextArea = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(10, 30), size=(520, 300))
  TextArea_2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=(10, 460), size=(520, 70))
  Button_Use_my_Suggestion_Discovery=wx.Button(panel,pos=(10,550),label="Use My Suggestion")
  Button_Use_my_Suggestion_Discovery.Hide()
  TextArea_2.Hide();
  for document in Documents:
    TextArea.AppendText("\n=============================================================\n")
    TextArea.AppendText(document)
    TextArea.AppendText("\n=============================================================\n")
  TextArea.SetFont(font1)
  label_Discovery_relevency=wx.StaticText(panel, label="Do you think Discovery has found correct documents :", pos=(5, 380))
  def onYesDiscovery(self):
    label_Discovery_relevency=wx.StaticText(panel, label="Thanks, We are glad that you are satisfied",pos=(100, 440))

  def onNoDiscovery(self):
    Label_Suggestion_discovery.Show()
    TextArea_2.Show()
    Button_Use_my_Suggestion_Discovery.Show()
    Button_Use_my_Suggestion_Discovery.Bind(wx.EVT_BUTTON, Train_Discovery)

  def Train_Discovery(self):
    content=TextArea_2.GetValue()
    TextArea_2.Hide()
    Label_Suggestion_discovery.Hide()
    label_sent_for_discovery = wx.StaticText(panel, label="Your suggestion has been submitted to Discovery:",pos=(100, 470))




  Button_Yes_Discovery=wx.Button(panel,pos=(10, 410), label="Yes")
  Button_Yes_Discovery.Bind(wx.EVT_BUTTON,onYesDiscovery)
  Button_No_Discovery=wx.Button(panel,pos=(400, 410), label="No")
  Button_No_Discovery.Bind(wx.EVT_BUTTON,onNoDiscovery)


  Frame_3.Show()
  #print(config.get('DISCOVERY_SECTION','Environment_id'),config.get('DISCOVERY_SECTION',collection+'_id'))
  #qopts = {'query': 'enriched_text.keywords.text:Netcool Performance Manager', 'filter': 'enriched_text.concepts.text::IBM'}
  #qopts = {'query': query, 'filter': 'text:API'}
  #my_query = discovery.query(config.get('DISCOVERY_SECTION', 'Environment_id'), collection, qopts)
  #print("                                               ")
  #print("Below is the output fetched from TNPM_COLLECTION")
  #print(json.dumps(my_query, indent=2))


