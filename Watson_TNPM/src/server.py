from flask import Flask,request,redirect,url_for,sessions, render_template
import json
import NLCservice_step4
import NLCservice
import csv
import requests
import url_mapper
import test_discovery
import operator
import configparser
from collections import defaultdict
import os
from os import path
import re


app = Flask(__name__)
Solution_list=[]
error_list=[]
Likes_list=[]
file_id_names = {}
Solution_problem_Like = defaultdict(dict)
Solution_problem_First = defaultdict(dict)
passage_list=[]
Passages={}
docurls=[]
data=''
@app.route('/',methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        data=request.form['textbox']
        #print(data)
        Solution_list=NLCservice_step4.classify_problem(data)
        #return render_template("NLCoutput.html", Solution_list=Solution_list)
        return redirect(url_for('NLC',Solution_list))
    else:
        #resp=render_template("Main_copy.html")
        like = 0
        #with open('D:/Watson/WATSON_TRAINING_DATA/problem_solution_likes.csv', 'r') as f:
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_likes.csv"))
        with open(filepath, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                Solution_problem_Like[row[1]][row[0]]= row[2]
        #resp=render_template("Final_Main_copy.html",Solution_problem_Like=Solution_problem_Like)
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_likes.csv"))
        with open(filepath, "r") as f1:
            reader = csv.reader(f1)
            for row in reader:
                Solution_problem_First[row[1]][row[0]]= row[2]
                break
        resp = render_template("Final_Main_copy.html", Solution_problem_Like=Solution_problem_Like,Solution_problem_First=Solution_problem_First)
        #return render_template("Final_Discovery.html", like=like)
        return resp

@app.route('/NLC',methods=['GET','POST'])
def NLC():
    if request.method == 'POST' and request.form['btn'] == 'submit your suggestion':
        suggestion=request.form['textArea1']
        suggestion.replace('*', '')
        suggestion = re.sub('\s+', ' ', suggestion.replace('\n', ' ').replace('\r', '')).strip()
        suggestion = re.sub("From.*Subject", '',suggestion.replace('*', '').replace('<', '').replace('>', '').replace('?', '').replace(',','').replace("’", "").replace("'", "").replace('®', '').replace('=', '').replace('-', '').replace('"', '').replace('•', '').replace('@', '').replace('//', '').replace('ó', '').replace('í', '').replace('ç', '').replace('ã', '').replace('é', '').replace('ú', '').replace('!', '').replace('õ', '').replace('à', '').replace('ô', '').replace('è', ''))
        query_asked=request.form['textArea2']
        #with open('D:/Watson/WATSON_TRAINING_DATA/training_data_Wireline_Latest_new.csv', 'a',newline='') as training_data:
        basepath = path.dirname(__file__)
        filepath = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "Clean_Wireline_training_data.csv"))
        with open(filepath,'a',newline='') as training_data:
            writer = csv.writer(training_data)
            writer.writerow([query_asked, suggestion])
        New_classfier = NLCservice.create_Classifier()
        #return render_template("NLC_2.html",New_classfier=New_classfier,query_asked=query_asked)
        return render_template("Final_NLC_2.html", New_classfier=New_classfier, query_asked=query_asked)
    elif request.method == 'POST' and request.form['btn'] == 'Find Solution':
        data = request.form['textbox']
        Solution_list = NLCservice_step4.classify_problem(data)
        size = len(Solution_list)
        #return render_template("testing.html", Solution_list=Solution_list, data=data,size=size)
        return render_template("final_testing_copy.html", Solution_list=Solution_list, data=data, size=size)

@app.route('/index3')
def index3():
    solution=request.args['solution']
    # print("hey buddy"+solution)
    data=request.args['data']
    like=0
    #return render_template("index3.html",solution=solution,data=data)
    #with open('D:/Watson/WATSON_TRAINING_DATA/problem_solution_likes.csv', 'r') as f:
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_likes.csv"))
    with open(filepath, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            #print(row[1])
            if solution == row[1]:
                like=row[2]
                #print(like)
    return render_template("final_index3.html", solution=solution, data=data,like=like)

@app.route('/index4',methods=['POST'])
def index4():
    #print(request.form['clicks'])
   # print(request.form['data'])
    #print(request.form['solution'])
    likes=request.form['clicks'];
    data=request.form['data']
    solution=request.form['solution']
    counter = 0;
    basepath = path.dirname(__file__)
    #with open('D:/Watson/WATSON_TRAINING_DATA/problem_solution_likes.csv', 'r') as f, open( 'D:/Watson/WATSON_TRAINING_DATA/problem_solution_newlikes.csv', 'a', newline='') as new_data:
    filepath = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_likes.csv"))
    filepath2 = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_newlikes.csv"))
    #filepath = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_likes.csv"))
    with open(filepath, "r") as f, open(filepath2, 'a', newline='') as new_data:
        reader = csv.reader(f)
        writer = csv.writer(new_data)
        writer_latest = csv.writer(new_data)
        #print("i am here")
        for row in reader:
            #print(row)
            if solution == row[1]:
                counter = counter + 1;
                writer.writerow([data, solution, likes])
            else:
                #print(row)
                writer.writerow(row)
    #os.remove('D:/Watson/WATSON_TRAINING_DATA/problem_solution_likes.csv')
   #os.rename('D:/Watson/WATSON_TRAINING_DATA/problem_solution_newlikes.csv','D:/Watson/WATSON_TRAINING_DATA/problem_solution_likes.csv')with open('D:/Watson/WATSON_TRAINING_DATA/problem_solution_newlikes_sorted.csv', 'a',newline='') as sorted_data:
    sample = open(filepath2, "r")
    csv1 = csv.reader(sample, delimiter=',')
    sort = sorted(csv1, key=operator.itemgetter(2),reverse=True)
    sample.close()
    filepath3 = path.abspath(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_newlikes_sorted.csv"))
    with open(filepath3, 'a', newline='') as sorted_data:
        for eachline in sort:
            writer = csv.writer(sorted_data)
            writer.writerow(eachline)
    os.remove(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_newlikes.csv"))
    os.remove(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_likes.csv"))
    os.rename(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_newlikes_sorted.csv"),path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_likes.csv"))
    if counter == 0:
        with open(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_likes.csv"), 'a', newline='') as new_training_data:
            writer = csv.writer(new_training_data)
            writer.writerow([data, solution, likes])
        sample = open(path.join(basepath, "..", "../WATSON_TRAINING_DATA", "problem_solution_likes.csv"),'r')
        csv1 = csv.reader(sample,delimiter=',')
        sort = sorted(csv1,key=operator.itemgetter(2))
    return ('', 204)

@app.route('/index5',methods=['POST'])
def index5():
    #print(request.form['clicks'])
   # print(request.form['query'])
   # print(request.form['url'])
   # print(request.form['document'])
    return ('', 204)

@app.route('/DISCOVERY',methods=['GET','POST'])
def DISCOVERY():
    if request.method == 'POST' and request.form['btn'] == 'Send_for_discovery':
                filter=request.form['filters']
                query = request.form['textArea3']
                #print(query)
                like = 0
                Documents=NLCservice_step4.get_Document_Suggestion(query,filter)
                #print(Documents)
                urls=url_mapper.classify_problem(Documents)
                #print(urls)
                filenames = []
                url_new = 'https://gateway.watsonplatform.net/discovery/api/v1/environments/fc80f619-8cfd-4131-962a-c6dd8944bbae/collections/9ca1a3fa-a90a-4e3c-ba84-1e1053bfbc75/query?return=extracted_metadata&version=2017-08-01'
                headers = {'content-type': 'application/json',
                           'Authorization': 'Basic ODE4NTdkOTAtNmNjZS00N2ZjLTk5N2MtYzdiMjZmMWEwMDg0OjhlOG5pSHJ4aWRLSA=='}
                response = requests.get(url_new, headers=headers)
                json_response = response.json()
                for result in json_response["results"]:
                    # filenames.append(result["extracted_metadata"]["filename"])
                    file_id_names[result["id"]] = result["extracted_metadata"]["filename"]
                    filenames.append(result["extracted_metadata"]["filename"])
                #return render_template("DISCOVERY.html",Documents=Documents,urls=urls,filenames=filenames,file_id_names=file_id_names,query=query)
                return render_template("Final_Discovery.html", Documents=Documents, urls=urls, filenames=filenames,
                                       file_id_names=file_id_names, query=query,like=like)
    elif request.method == 'POST' and request.form['btn'] == 'Use_My_Suggestion':
                content = request.form['textArea9']
                key = '';
                for k, v in file_id_names.items():
                    if v == content:
                        key = k
                        #print(key)
                with open("D:/Watson/training_example_new_1.json", 'r') as f:
                    data = json.load(f)
                    # print(data)
                    f.close()
                    data['natural_language_query'] = request.form['textArea11']
                    # print(data)
                    for example in data["examples"]:
                        example["document_id"] = key
                        example["relevance"] = 10
                with open("D:/Watson/training_example_new_1.json", 'w+') as f:
                    f.write(json.dumps(data, indent=4))
                    f.close()
                url_new = 'https://gateway.watsonplatform.net/discovery/api/v1/environments/fc80f619-8cfd-4131-962a-c6dd8944bbae/collections/9ca1a3fa-a90a-4e3c-ba84-1e1053bfbc75/training_data?version=2017-08-01'
                payload = json.load(open("D:/Watson/training_example_new_1.json"))
                payload_new = json.dumps(payload, indent=4)
                headers = {'content-type': 'application/json',
                           'Authorization': 'Basic ODE4NTdkOTAtNmNjZS00N2ZjLTk5N2MtYzdiMjZmMWEwMDg0OjhlOG5pSHJ4aWRLSA=='}
                requests.post(url_new, data=payload_new, headers=headers)
                return render_template("final.html")

@app.route('/PASSAGES',methods=['GET','POST'])
def PASSAGES():
    if request.method == 'POST' and request.form['btn1'] == 'Look for Passages':
        filter = request.form['filters1']
        query = request.form['textArea4']
        # print(query)
        #like = 0
        Passages = test_discovery.get_Document_Suggestion(query, filter)
        passage_list=Passages.keys();
        config = configparser.RawConfigParser()
        config.read('configfile.properties')
        for passage in passage_list:
            docurls.append(config.get('ID_TO_URL_SECTION',passage))
           # print(passage)
           # print(Passages.get(passage))
        #URL = config.get('ID_TO_URL_SECTION', Passage)
        #print(docurls)
        #print(Passages)
        return render_template("Passage.html", docurls=docurls, Passages=Passages,query=query)

    @app.route('/Log_Analyzer', methods=['GET', 'POST'])
    def Log_Analyzer():
        file = open("textfile.txt", "w")
        file.write(request.form['contents'])
        file.close();
        with open("textfile.txt") as f:
            for line in f:
                if "ACQUISITION_ERROR" in line:
                    error_list.append(line)
        return render_template("Analyzer_output.html")


if __name__=="__main__":
    #app.run(debug=True,use_reloader=True)
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    app.run(host='0.0.0.0')