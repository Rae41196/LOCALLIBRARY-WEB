from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name = 'index'), #view function that will be called if the URL pattern is detected: views.index,  which is the function named index()
    
]