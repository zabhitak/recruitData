from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('xgboostmo.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Source_Type=1
    Edu_Type=1
    if request.method == 'POST':
        Education = int(request.form['Education'])

        if(Education=='1'):
            Edu_Type=4
        elif Education=='2':
            Edu_Type=5
        elif Education=='3':
            Edu_Type=2
        elif Education=='5':
            Edu_Type=3
        else:
            Edu_Type=1


        CGPA=float(request.form['CGPA'])
        Experience=int(request.form['Experience'])
        SourceId=request.form['SourceId']

        if(SourceId=='Indeed'):
            Source_Type=1
        elif SourceId=='Shine':
            Source_Type=2
        elif SourceId=='Naukri':
            Source_Type=3
        elif SourceId=='LinkedIn':
            Source_Type=4
        elif SourceId=='Consultant2':
            Source_Type=5
        else:
            Source_Type=6
       
        d = {'QualLevel': [Edu_Type], 'CGPA': [CGPA],'CurrentExperience': [Experience], 'SourceId': [Source_Type]}
        de = pd.DataFrame(data=d)
        prediction=model.predict(de)
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry wrong input try again")
        else:
            if output == 3:
                output = 95
            if output == 2:
                output = 80
            if output == 1:
                output = 65
            return render_template('index.html',prediction_text="Your Chances of selection are {} %".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

