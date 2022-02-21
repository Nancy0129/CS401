from flask import Flask
import pickle
import numpy as np
from flask import Flask, request, jsonify
import os, time

app = Flask(__name__)

with open('ML.pickle','rb') as f:
    app.model=pickle.load(f)
    app.t=pickle.load(f)
    app.v=pickle.load(f)

app.CV = pickle.load(open("CV.pickle", "rb"))
app.TF = pickle.load(open("TF.pickle", "rb"))

@app.route("/api/american", methods=["POST"])
def prediction():
    content=request.get_json(force=True)
    text=np.array([content['text']])
    textCV=app.CV.transform(text)
    textTF=app.TF.transform(textCV)
    pre=app.model.predict(textTF)
    
    
    
    return jsonify({"is_american":str(pre[0]),"version":app.v," model_date":app.t})
