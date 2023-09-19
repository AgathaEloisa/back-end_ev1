from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'menuApp'

urlpatterns = [
    path('', vistaMenuView.as_view(), name='home')
]
