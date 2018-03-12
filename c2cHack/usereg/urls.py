from django.urls import path
from .views import getRegPage,addUser

urlpatterns = [
    path('', getRegPage, name='usereg'),
    path('register/', addUser, name='register')
]