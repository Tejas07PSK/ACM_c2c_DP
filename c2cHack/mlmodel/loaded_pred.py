# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 22:10:28 2018

@author: Nabarun Chatterjee
"""
import pickle
from .load_data import files_import
import numpy as np
import os

app_dir = os.path.dirname(__file__)

symptom,diagnosis,symp_vs_diag = files_import()

tmdl = pickle.load(open(os.path.join(app_dir, 'finalized_model.sav'), 'rb'))
weights = np.load(os.path.join(app_dir, 'arraywei.npy'))
z = 0
slist = [0 for x in range(54)]

def to_matrix(l):
    return [l]

def appendSymptoms(symp):
    global z, symptom, slist
    for i in range(0, len(symptom)):
        if symptom['symptom'][i] == 'symptom':
            continue
        else:
            if symptom['symptom'][i] == symp:
                    slist[z] = symptom['syd'][i]
                    z += 1

def getMostProbDisease():
    global slist, tmdl, diagnosis, z
    slist = to_matrix(slist)
    a = np.array(slist)
    a.sort(axis=1)
    kpred = tmdl.predict(a)
    for i in range(0,len(diagnosis)):
        if diagnosis['did'][i] == 'did':
            continue
        else:
            if diagnosis['did'][i] == kpred:
                z=0
                slist = [0 for x in range(54)]
                return diagnosis['diagnose'][i],weights[i]