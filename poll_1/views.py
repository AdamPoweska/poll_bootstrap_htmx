# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, TemplateView, ListView, UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import *

class MainPageView(TemplateView):
    template_name = 'main_page.html'


class QuestionA(FormView):
    template_name = 'quiz_1_question_1.html'
    form_class = QuizOneQuestionOne
    success_url = reverse_lazy('quiz_1_question_2')


class QuestionB(FormView):
    template_name = 'quiz_1_question_2.html'
    form_class = QuizOneQuestionTwo
    success_url = reverse_lazy('quiz_1_question_3')


class QuestionC(FormView):
    template_name = 'quiz_1_question_3.html'
    form_class = QuizOneQuestionThree
