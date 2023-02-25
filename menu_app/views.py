from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def menu(request):
    if request.method == 'GET':
        return render(request, template_name='menu/index.html')
