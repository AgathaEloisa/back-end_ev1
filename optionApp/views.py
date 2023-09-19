from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import random

class vistaTablaViews(View):
    def get(self, request, *args, **kwargs):
        countries = [{
            'country':'Irlanda',
            'continent': 'Europa',
            'flag': '/static/img/irlanda.png'
        },
        {
            'country':'Canadá',
            'continent': 'América del norte',
            'flag': '/static/img/canada.png'
        },
        {
            'country':'Argentina',
            'continent': 'América del sur',
            'flag': '/static/img/argentina.png'
        }]

        context = {
            'countries' : countries
        }
        
        html_content =  render(request, 'optionApp/vistaTabla.html', context)
        return HttpResponse(html_content)
    
class vistaLoteriaViews(View):
    def get(self, request, *args, **kwargs):
        randomList = [random.randint(1,100) for _ in range(10)]
        orderedNumbers = sorted(randomList)
        context = {
            'orderedNumbers' : orderedNumbers
            }
        html_content =  render(request, 'optionApp/vistaLoteria.html', context)
        return HttpResponse(html_content)