from flask import Flask
import pickle
import numpy as np
from flask import Flask, request, jsonify
import os, time

app = Flask(__name__)
app.model = pickle.load(open("ML.pickle", "rb"))
app.CV = pickle.load(open("CV.pickle", "rb"))
app.TF = pickle.load(open("TF.pickle", "rb"))
time_local = time.localtime(os.path.getmtime("ML.pickle"))
app.dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
@app.route("/api/american", methods=["POST"])
def prediction():
    content=request.get_json(force=True)
    text=np.array([content['text']])
    textCV=app.CV.transform(text)
    textTF=app.TF.transform(textCV)
    pre=app.model.predict(textTF)
    
    
    
    return jsonify({"is_american":str(pre[0]),"version":"MultinomialNB_v1"," model_date":app.dt})


