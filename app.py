import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import os

app = Flask(__name__)
models = pickle.load(open('models.pckl', 'rb'))
grids_pdfs = pickle.load(open('grids_pdfs.pckl', 'rb'))

@app.route('/',methods=["GET","POST"])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    g = float(request.form.get("Irradiance"))
    t = float(request.form.get("Temperature"))
    i = int(request.form.get("Grid id"))
    obs_power = float(request.form.get("Measured power"))
    f = [g**3, g**2, (g**2)*t, g*(t**2), g*t, g]
    prediction = models[i].predict(np.array(f).reshape(1, -1))
    if (float(prediction) - obs_power)<grids_pdfs[i][0] or (float(prediction) - obs_power) > grids_pdfs[i][1]:
    	Error = 'Malfunction detected'
    else:
    	Error = 'The error is in the confidence interval (95%)'

    return render_template('index.html', prediction_text='The AC power should be: {}'.format(str(round(prediction[0], 2))), Error = '{}'.format(Error))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
