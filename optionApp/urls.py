from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'optionApp'

urlpatterns = [
    path('vistaTabla', vistaTablaViews.as_view(), name='vistaTabla'),
    path('vistaLoteria', vistaLoteriaViews.as_view(), name='vistaLoteria')
]
