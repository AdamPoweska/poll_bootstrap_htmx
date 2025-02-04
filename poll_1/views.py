# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, TemplateView, ListView, UpdateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.db.models import Count
from collections import defaultdict

from .forms import *
from .models import *


class MainPageView(TemplateView):
    template_name = 'main_page.html'


class QuestionA(FormView):
    template_name = 'quiz_1_question_1.html'
    form_class = QuizOneQuestionOne
    success_url = reverse_lazy('quiz_1_question_2')

    def form_valid(self, form):
        answer = form.cleaned_data['question_one_select']
        SurveyOneResponses.objects.create(question='Question 1', answer=answer) # zapisanie do modelu i bazy danych, forms nie zapisują do bazy danych - tylko modele
        return super().form_valid(form)


class QuestionB(FormView):
    template_name = 'quiz_1_question_2.html'
    form_class = QuizOneQuestionTwo
    success_url = reverse_lazy('quiz_1_question_3')

    def form_valid(self, form):
        answer = form.cleaned_data['question_two_select']
        SurveyOneResponses.objects.create(question='Question 2', answer=answer)
        return super().form_valid(form)


class QuestionC(FormView):
    template_name = 'quiz_1_question_3.html'
    form_class = QuizOneQuestionThree
    success_url = reverse_lazy('quiz_1_results')

    def form_valid(self, form):
        answer = form.cleaned_data['question_three_select']
        SurveyOneResponses.objects.create(question='Question 3', answer=answer)
        return super().form_valid(form)

class SurveyOneResults(ListView):
    model = SurveyOneResponses
    template_name = 'quiz_1_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # pobieranie i grupowanie odpowiedzi
        summary = (
            SurveyOneResponses.objects
            .values('question', 'answer')
            .annotate(count=Count('answer'))
            .order_by('question')
        )

        # grupowanie odpowiedzi wg. pytań
        grouped_responses = defaultdict(list)
        question_totals = defaultdict(int)

        for response in summary:
            question = response['question']
            grouped_responses[question].append(response)
            question_totals[question] += response['count']
        
        for question, responses in grouped_responses.items():
            total_responses = question_totals[question]
            for response in responses:
                response['percentage'] = (response['count'] / total_responses) * 100
        
        QUESTION_TITLES = {
            "Question 1": "What do you value most in your work?",
            "Question 2": "What motivates you to work?",
            "Question 3": "What would you change in the company?"
        }

        renamed_grouped_responses = {}
        for question, responses in grouped_responses.items():
            new_title = QUESTION_TITLES.get(question, question)  # jeśli nic nie będzie to zostanie stara nazwa
            renamed_grouped_responses[new_title] = responses
        
        
        context['grouped_responses'] = dict(renamed_grouped_responses)
        context['question_totals'] = dict(question_totals)

        return context
