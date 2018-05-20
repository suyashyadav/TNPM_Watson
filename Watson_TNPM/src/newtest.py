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

app = Flask(__name__)

@app.route('/Log_Analyzer',methods=['GET','POST'])
def Log_Analyzer():
    return render_template("Analyzer_output.html")

if __name__=="__main__":
    app.run(debug=True,use_reloader=True)