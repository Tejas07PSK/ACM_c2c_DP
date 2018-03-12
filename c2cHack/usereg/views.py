from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import UserDetails,generateId
from .forms import UsrRegForm


# Create your views here.

def getRegPage(request):
    usrRgFrm = UsrRegForm()
    return HttpResponse((loader.get_template('usereg/index.html')).render({'form': usrRgFrm}, request))

def addUser(request):
     us = UsrRegForm(request.POST)
     if (us.is_valid()):
         usr = us.save(commit=False)
         if(usr.pss==request.POST.get('pss_chk', 'empty')):
             usr.save()
             return render(request, 'usereg/index.html', {'form': UsrRegForm(), 'data': "Sussessfully Registered!!", 'col_code': '1'})
         else:
             return render(request, 'usereg/index.html', {'form': UsrRegForm(), 'data': "Registration Unsuccessful!!", 'col_code': '0'})
     else:
         return render(request, 'usereg/index.html', {'form': UsrRegForm(), 'data': "Registration Unsuccessful!!", 'col_code': '0'})

