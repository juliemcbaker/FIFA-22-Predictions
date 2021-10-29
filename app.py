from flask import Flask, render_template, jsonify, redirect, request
import pickle
import numpy as np
import pymongo
from password import password
import certifi


ca=certifi.where()
conn = f'mongodb+srv://aarvin:{password}@cluster0.j8pgj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(conn, tlsCAFile=ca)
db = client.fifadb

with open('models/clr0.sav', 'rb') as f: 
	rfr=pickle.load(f)

with open('models/scaler.sav', 'rb') as f: 
	scaler=pickle.load(f)


#try your actual code here

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetch')
def fetch():
    data=db.fifa.find_one()
    result_json={key:value for (key,value) in data.items() if key!='_id'}
    return jsonify(result_json)


@app.route('/player_stats/<fullname>')
def fetch_player(fullname):
    return_obj={}
    data=db.fifa.find_one()
    for idx, value in data['FullName'].items(): 
        if value==fullname: 
            break
    for each_attr in data.keys(): 
        if each_attr !='_id': 
            return_obj[each_attr]=data[each_attr][idx]
    return jsonify(return_obj)

@app.route('/sample/<query_string>')
@app.route('/sample<query_string>')
def sample(query_string): 

    # input_array = query_string.split("&")
    # for (i=0; i<input_array.length; i++) {
    #     console.log(input_array[i].split("=")[0], input_array[i].split("=")[1]);
    # }
    # output=request.args.get('Age', '')
    # #console.log(output)
    # return jsonify({'Inputs': query_string, 'Results': output})
    # parse_str($query_string, $get_array);
    # print_r($get_array);
    # #input_array=np.ndarray(query_string)
    # scaled_input=scaler.transform([input_array])
    # # input_ary=[inputs[sample_input] if (sample_input in inputs) else 0 for sample_input in scaler]
    # # input_scaled=scaler.transform([input_ary])
	# # prediction=rfr.predict(input_scaled)
    # #return jsonify({'input(s)': inputs, 'output': round(rfr.predict(input_scaled)[0], 2)})
    # prediction=rfr.predict(scaled_input)
    return jsonify({'output': 'hi'})

def fetch_player(fullname):
    return_obj={}
    data=db.fifa.find_one()
    for idx, value in data['FullName'].items(): 
        if value==fullname: 
            break
    for each_attr in data.keys(): 
        if each_attr !='_id': 
            return_obj[each_attr]=data[each_attr][idx]
    return return_obj

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # {"Attribute":"Defending",
    # "input_ball":"0",
    # "input_composure":"0",
    # "input_defend":"0",
    # "input_pace":"0",
    # "input_pass":"0",
    # "input_position":"0"}
    statdata = fetch_player(request.form.get("input_playername"))
    inputs={'Composure': int(request.form.get('input_composure')),
                'Positioning': int(request.form.get('input_position')),
                'BallControl': int(request.form.get('input_ball')),
                'PaceTotal': int(request.form.get('input_pace')),
                'ShortPassing': int(request.form.get('input_pass'))
               }

    return jsonify({'input(s)': inputs, 'output': round(rfr.predict(input_scaled)[0],2)})
    
    #inputs.update({column_dict[name]:1 for name in cat_inputs.values() if name in column_dict.keys()})
    # input_ary=[inputs[each_feature] if (each_feature in inputs) else 0 for each_feature in input_columns]
    # input_scaled=scaler.transform([input_ary])
    
    
    return jsonify(inputs)

# @app.route('/predict')
# def predict():
#     inputs={'Defending': request.form('Defending', 0)}
#     cat_inputs={'Composure': request.form('Composure'),
#                 'Positioning': requests.form('Positioning'),
#                 'BallControl': requests.form('BallControl'),
#                 'PaceTotal': requests.form('PaceTotal'),
#                 'ShortPassing': requests.form('ShortPassing')}
#     inputs.update({column_dict[name]:1 for name in cat_inputs.values() if name in column_dict.keys()})
#     input_ary=[inputs[each_feature] if (each_feature in inputs) else 0 for each_feature in input_columns]
#     input_scaled=scaler.transform([input_ary])
#     return jsonify({'input(s)': inputs, 'output': round(rfr.predict(input_scaled)[0],2)})

# @app.route('/predict_overall/')
# @app.route('/predict_overall')
# def predict_overall():
#     Composure=request.args.get('Composure')
#     Positioning=requests.args.get('Positioning')
#     BallControl=requests.args.get('BallControl')
#     PaceTotal=requests.args.get('PaceTotal')
#     ShortPassing=requests.args.get('ShortPassing')
#     scaler_input=scaler.transform([[scaler]]).toarray()

#     prediction=rfr.predict([scaler_input])
#     return render_template('index.html')
#     return jsonify({'input(s)': inputs, 'output': round(rfr.predict(input_scaled)[0],2)}) """

#steps from tutor
       #predictions go here (all selections into array of arrays)
       #load model (pickle.load)
       #model.predict (store model into variable)
       #pass back to index.html
    #    prediction=0
    # return render_template('index.html', prediction=prediction) '''


    #use transformed input to predict
if __name__=='__main__':
    app.run()