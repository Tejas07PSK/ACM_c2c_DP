# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 20:00:16 2018

@author: Nabarun Chatterjee
"""
import pandas as pd
# import the files
import os

app_dir = os.path.dirname(__file__)

def files_import():
    global app_dir
    symptom = pd.read_csv(os.path.join(app_dir, 'symptoms.csv'))
    diagnosis = pd.read_csv(os.path.join(app_dir, 'diagnosis.csv'))
    symp_vs_diag = pd.read_csv(os.path.join(app_dir, 'diagnosis_vs_symptoms.csv'))
    print("Data Loaded")
    return symptom,diagnosis,symp_vs_diag