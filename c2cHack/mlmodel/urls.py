from django.urls import path
from .views import getPredPage,getJsnRespForMl,getTechStack

urlpatterns = [
    path('', getPredPage, name='predictor'),
    path('predict/', getJsnRespForMl, name='predict'),
    path('stack/', getTechStack, name='stack')
]