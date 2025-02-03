from django import forms

class QuizOneQuestionOne(forms.Form):
    QUESTION_CHOICES = [
        ('q1', 'Question 1'),
        ('q2', 'Question 2'),
        ('q3', 'Question 3'),
        ('q4', 'Question 4'),
    ]

    question_one_select = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )


class QuizOneQuestionTwo(forms.Form):
    QUESTION_CHOICES = [
        ('q1', 'Question 5'),
        ('q2', 'Question 6'),
        ('q3', 'Question 7'),
        ('q4', 'Question 8'),
    ]

    question_two_select = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )


class QuizOneQuestionThree(forms.Form):
    QUESTION_CHOICES = [
        ('q1', 'Question 9'),
        ('q2', 'Question 10'),
        ('q3', 'Question 11'),
        ('q4', 'Question 12'),
    ]

    question_three_select = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )