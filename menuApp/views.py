from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class vistaMenuView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        html_content = render(request, 'menuApp/vistaMenu.html', context)
        return HttpResponse(html_content)