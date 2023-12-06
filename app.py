# -*- coding: utf-8 -*-
 

from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('gridmodel.pkl')

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    gender = request.form['gender']
    age = int(request.form['age'])
    salary = int(request.form['salary'])

    print(f"Gender: {gender}, Age: {age}, Salary: {salary}")
    
    if gender=='Male':
        g=1
    else:
        g=0
    # Make a prediction using your model
    prediction = model.predict([[age,salary,g]])

    print(f"Raw Prediction: {prediction}")
    # You can customize this part based on your model's output
    if prediction[0] == 1:
        result = "Yes, the person can buy a car."
    else:
        result = "No, the person cannot buy a car."
    print(result) 
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
