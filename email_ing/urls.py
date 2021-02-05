from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.indexView, name='form'),
    path('success', views.successView, name='success')

]
