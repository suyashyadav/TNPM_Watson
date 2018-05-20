from flask import Flask,request, render_template
import json
#import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("Jquery_test.html")

@app.route('/receivedata',methods=['GET','POST'])
def receive_data():
    if request.method == 'POST':
        print(request.form['myData'])
        render_template("profiles.html")


if __name__=="__main__":
    app.run(debug=True,use_reloader=False)