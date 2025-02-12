# Create your models here.

from django.db import models

class SurveyOneResponses(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.question}: {self.answer}"


