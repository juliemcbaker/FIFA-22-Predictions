from flask import Flask, render_template, jsonify, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def choices():
    if request.method=='POST':
       SprintSpeed= request.form['SprintSpeed']
       Composure= request.form['Composure']
       #predictions go here (all selections into array of arrays)
       #load model (pickle.load)
       #model.predict (store model into variable)
       #pass back to index.html
       prediction=0
    return render_template('index.html', prediction=prediction)


    #use transformed input to predict
if __name__=='__main__':
    app.run()