# Create your views here.

from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.db.models import Count
from collections import defaultdict

from .forms import *
from .models import SurveyOneResponses


class MainPageView(TemplateView):
    template_name = 'main_page.html'

class SecondSurvey(TemplateView):
    template_name = 'quiz_2.html'

class QuestionA(FormView):
    template_name = 'quiz_1_question_1.html'
    form_class = QuizOneQuestionOne
    success_url = reverse_lazy('quiz_1_question_2')

    # zapisanie do modelu i bazy danych, forms nie zapisują do bazy danych - tylko modele
    def form_valid(self, form):
        answer = form.cleaned_data['question_one_select'] # forms "QuizOneQuestionOne" > choicefield "question_one_select" <- przekazanie cleaned data z htmlu do forms
        SurveyOneResponses.objects.create(question='Question 1', answer=answer) # stworzenie objektu za pomocą modelu SurveyOneResponses
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

        # Query Set - podejście SQL'a raczej się nie opłaca na tak małą bazę danych
        summary = (
            SurveyOneResponses.objects
            .values('question', 'answer') # .values pozwala na zwrócenie danych jako słowników a nie jako obiektów modelu
            .annotate(count=Count('answer')) # .annotate dodaje dodatkowe pola do obiektów pól zwracanych przez zapytania do baz danych (query set) - w tym przypdaku jest to variable count używajacy funckji Count -> która to liczy powiązane obiekty w bazie danych
            .order_by('question')
        )

        # dict, które przekażemy do html'a
        grouped_responses = defaultdict(list) # defaultdict(list) - tworzy domyślną wartość jako pustą listę dla nowego klucza -> można dodawać elementy bez sprawdzania czy klucz istnieje
        question_totals = defaultdict(int)

        for response in summary: # dla każdej odpowiedzi w zbiorze danych z SurveyOneResponses
            question = response['question'] # bazując na wartości 'question' z każdego 'response'
            grouped_responses[question].append(response) # dodajemy response do słownika 
            question_totals[question] += response['count'] # dodajemy count do słownika totals - przekaże liczbę kliknięć w daną odpowiedź
        
        for question, responses in grouped_responses.items():
            total_responses = question_totals[question] # liczba wszystkich odpowiedzi (.items) dla danego pytania (question) ze słownika question_totals
            for response in responses:
                response['percentage'] = (response['count'] / total_responses) * 100
        
        # nadanie ładnych opisów - inaczej będziemy mieć tylko 'Question 1' itd -> z bazy danych
        QUESTION_TITLES = {
            "Question 1": "What do you value most in your work?",
            "Question 2": "What motivates you to work?",
            "Question 3": "What would you change in the company?"
        }

        renamed_grouped_responses = {}
        for question, responses in grouped_responses.items():
            new_title = QUESTION_TITLES.get(question, question) # .get zwraca wartość dla przekazanego klucza. "value = dictionary.get(key, default_value)" <- dlatego mamy question, question
            renamed_grouped_responses[new_title] = responses # tworzymy nowy słownik z ładnymi nazwami ale wartościami z poprzedniego słownika
        
        
        context['grouped_responses'] = dict(renamed_grouped_responses) # wcześniej używam defaultdict - obiekty tej instancji zachowują się jak słowniki, ale mają domyślną wartość dla nieistniejących kluczy - może to powodować error i dlatego lepiej jeszcze raz zabezpieczyć się "dict()"
        context['question_totals'] = dict(question_totals)

        return context
