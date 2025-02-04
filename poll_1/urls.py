from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name="main_page"),
    path('quiz_1_question_1/', views.QuestionA.as_view(), name="quiz_1_question_1"),
    path('quiz_1_question_2/', views.QuestionB.as_view(), name="quiz_1_question_2"),
    path('quiz_1_question_3/', views.QuestionC.as_view(), name="quiz_1_question_3"),
    path('quiz_1_results/', views.SurveyOneResults.as_view(), name="quiz_1_results"),
    path('quiz_2/', views.SecondSurvey.as_view(), name="quiz_2"),
]