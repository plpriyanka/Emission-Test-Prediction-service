#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:33:50 2017

@author: priyanka
"""

from sklearn.externals import joblib as jl
import pandas as pd
from flask import Flask
from flask import request
app = Flask(__name__)

clf = jl.load('trained_model.pkl')

def predict_emission_test(carInputData):
    features = pd.DataFrame(carInputData)
    
    result = clf.predict(features)
    
    if result[0] == 1:
        return 'Your car condition is good. Enjoy :)'
    else:
        return 'Oops Your car condition is bad. It might fail in emissions test :('

@app.route('/check/forpasscar', methods=['GET'])
def predict_emission_test_for_pass_car():
    # show the user profile for that user
    v_make = request.args.get('v_make', 'VW')
    v_model_year = request.args.get('v_model_year', '')
    v_gvwr = request.args.get('v_gvwr', '')
    v_obd_misfire = request.args.get('v_obd_misfire', '')
    v_obd_evap = request.args.get('v_obd_evap', '')
    v_obd_secair = request.args.get('v_obd_secair', '')
    v_obd_o2sensor = request.args.get('v_obd_o2sensor', '')
    v_obd_o2heater = request.args.get('v_obd_o2heater', '')
    v_obd_egr = request.args.get('v_obd_egr', '')
    
    carInputDataForPass = {
        0 : pd.Series( 0.6 , index=[0]),
        1 : pd.Series( 0.7 , index=[0]),
        2 : pd.Series( 0.250250393475 , index=[0]),
        3 : pd.Series( 0.0 , index=[0]),
        4 : pd.Series( 0.25 , index=[0]),
        5 : pd.Series( 0.4 , index=[0]),
        6 : pd.Series( 0.0 , index=[0]),
        7 : pd.Series( 0.4 , index=[0]),
        8 : pd.Series( 0.2 , index=[0]),
        9 : pd.Series( 0.2 , index=[0]),
        10 : pd.Series( 0.0 , index=[0]),
        11 : pd.Series( 0.0 , index=[0]),
        12 : pd.Series( 0.0 , index=[0]),
        13 : pd.Series( 0.0 , index=[0]),
        14 : pd.Series( 0.0 , index=[0]),
        15 : pd.Series( 0.0 , index=[0]),
        16 : pd.Series( 0.0 , index=[0]),
        17 : pd.Series( 0.0 , index=[0]),
        18 : pd.Series( 0.0 , index=[0]),
        19 : pd.Series( 0.0 , index=[0]),
        20 : pd.Series( 0.0 , index=[0]),
        21 : pd.Series( 0.0 , index=[0]),
        22 : pd.Series( 0.0 , index=[0]),
        23 : pd.Series( 0.0 , index=[0]),
        24 : pd.Series( 0.0 , index=[0]),
        25 : pd.Series( 0.0 , index=[0]),
        26 : pd.Series( 0.0 , index=[0]),
        27 : pd.Series( 0.0 , index=[0]),
        28 : pd.Series( 0.0 , index=[0]),
        29 : pd.Series( 0.0 , index=[0]),
        30 : pd.Series( 0.0 , index=[0]),
        31 : pd.Series( 0.0 , index=[0]),
        32 : pd.Series( 0.0 , index=[0]),
        33 : pd.Series( 0.0 , index=[0]),
        34 : pd.Series( 1.0 , index=[0]),
        35 : pd.Series( 0.0 , index=[0]),
        36 : pd.Series( 0.0 , index=[0]),
        37 : pd.Series( 0.0 , index=[0]),
        38 : pd.Series( 0.0 , index=[0]),
        39 : pd.Series( 0.0 , index=[0])
    }
    
    return predict_emission_test(carInputDataForPass)

@app.route('/check/forfailcar', methods=['GET'])
def predict_emission_test_for_fail_car():
    # show the user profile for that user
    v_make = request.args.get('v_make', 'VW')
    v_model_year = request.args.get('v_model_year', '')
    v_gvwr = request.args.get('v_gvwr', '')
    v_obd_misfire = request.args.get('v_obd_misfire', '')
    v_obd_evap = request.args.get('v_obd_evap', '')
    v_obd_secair = request.args.get('v_obd_secair', '')
    v_obd_o2sensor = request.args.get('v_obd_o2sensor', '')
    v_obd_o2heater = request.args.get('v_obd_o2heater', '')
    v_obd_egr = request.args.get('v_obd_egr', '')
    
    carInputDataForFail = {
        0 : pd.Series( 0.2 , index=[0]),
        1 : pd.Series( 0.1 , index=[0]),
        2 : pd.Series( 0.125053655745 , index=[0]),
        3 : pd.Series( 0.0 , index=[0]),
        4 : pd.Series( 0.25 , index=[0]),
        5 : pd.Series( 0.2 , index=[0]),
        6 : pd.Series( 0.0 , index=[0]),
        7 : pd.Series( 0.2 , index=[0]),
        8 : pd.Series( 0.2 , index=[0]),
        9 : pd.Series( 0.2 , index=[0]),
        10 : pd.Series( 0.0 , index=[0]),
        11 : pd.Series( 1.0 , index=[0]),
        12 : pd.Series( 0.0 , index=[0]),
        13 : pd.Series( 0.0 , index=[0]),
        14 : pd.Series( 0.0 , index=[0]),
        15 : pd.Series( 0.0 , index=[0]),
        16 : pd.Series( 0.0 , index=[0]),
        17 : pd.Series( 0.0 , index=[0]),
        18 : pd.Series( 0.0 , index=[0]),
        19 : pd.Series( 0.0 , index=[0]),
        20 : pd.Series( 0.0 , index=[0]),
        21 : pd.Series( 0.0 , index=[0]),
        22 : pd.Series( 0.0 , index=[0]),
        23 : pd.Series( 0.0 , index=[0]),
        24 : pd.Series( 0.0 , index=[0]),
        25 : pd.Series( 0.0 , index=[0]),
        26 : pd.Series( 0.0 , index=[0]),
        27 : pd.Series( 0.0 , index=[0]),
        28 : pd.Series( 0.0 , index=[0]),
        29 : pd.Series( 0.0 , index=[0]),
        30 : pd.Series( 0.0 , index=[0]),
        31 : pd.Series( 0.0 , index=[0]),
        32 : pd.Series( 0.0 , index=[0]),
        33 : pd.Series( 0.0 , index=[0]),
        34 : pd.Series( 0.0 , index=[0]),
        35 : pd.Series( 0.0 , index=[0]),
        36 : pd.Series( 0.0 , index=[0]),
        37 : pd.Series( 0.0 , index=[0]),
        38 : pd.Series( 0.0 , index=[0]),
        39 : pd.Series( 0.0 , index=[0])
    }
    
    return predict_emission_test(carInputDataForFail)