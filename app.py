from flask import Flask, render_template, jsonify, redirect, request
import pickle
import numpy as np

with open('models/clr0.sav', 'rb') as f: 
	scaler=pickle.load(f)

with open('models/scaler.sav', 'rb') as f: 
	scaler=pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def choices():
    if request.method=='POST':
       Defending= request.form['Defending']
       Composure= request.form['Composure']
       Positioning=requests.form['Positioning']
       BallControl=requests.form['BallControl']
       PaceTotal=requests.form['PaceTotal']
       ShortPassing=requests.form['ShortPassing']
       #predictions go here (all selections into array of arrays)
       #load model (pickle.load)
       #model.predict (store model into variable)
       #pass back to index.html
       prediction=0
    return render_template('index.html', prediction=prediction)


    #use transformed input to predict
if __name__=='__main__':
    app.run()