# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:22:07 2023

@author: rithe
"""

from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np



app=Flask(__name__)
cors=CORS(app)
model=pickle.load(open('grid.pkl','rb'))
car=pd.read_csv('car_data.csv')

@app.route('/',methods=['GET','POST'])
def index():
    Gender=sorted(car['Gender'].unique())
    Age=sorted(car['Age'].unique())
    AnnualSalary=sorted(car['AnnualSalary'].unique())
    

    #companies.insert(0,'Select Company')
    return render_template('index.html',Gender=Gender, Age=Age,AnnualSalary=AnnualSalary)


@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    Gender=request.form.get('Gender')

    
    AnnualSalary=request.form.get('AnnualSalary') 
    Age=request.form.get('Age')
    '''if(Gender=="Male"):
        g=1
    else:
        g=0'''

        
    

    prediction=model.predict(pd.DataFrame(columns=[ 'Age','AnnualSalary','Gender'],
                              data=np.array([Age,AnnualSalary,Gender]).reshape(1, 3)))
    print(prediction)

    return str(np.round(prediction[0],2))



if __name__=='__main__':
    app.run()