from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import json
from .loaded_pred import *

def getJsnRespForMl(request):
    if request.method == 'GET':
        v=request.GET.get('symps','empty')
        v=v.strip()
        lst=[]
        for i in v.split('\n'):
            for j in i.split(','):
                lst.append(j)
        print(str(lst))
        for sym in lst:
            appendSymptoms(sym)
        pds,svr=getMostProbDisease()
        jsn_dict={'PredDis': pds,'Sev':svr}
        json_string = json.dumps(jsn_dict)
        print(json_string)
        return HttpResponse(json_string, content_type="application/json")

def getPredPage(request):
    return HttpResponse((loader.get_template('mlmodel/predict_page.html')).render({}, request))

def getTechStack(request):
    return HttpResponse((loader.get_template('mlmodel/techstack.html')).render({}, request))
