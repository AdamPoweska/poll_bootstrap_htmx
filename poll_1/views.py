# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, TemplateView, ListView, UpdateView

# def index(request):
#     return HttpResponse("hello to poll app")

class MainPageView(TemplateView):
    template_name = 'main_page.html'

