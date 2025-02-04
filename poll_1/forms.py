from django import forms

class QuizOneQuestionOne(forms.Form):
    QUESTION_CHOICES = [
        ('Answer 1', 'Answer 1'),
        ('Answer 2', 'Answer 2'),
        ('Answer 3', 'Answer 3'),
        ('Answer 4', 'Answer 4'),
    ]

    question_one_select = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )


class QuizOneQuestionTwo(forms.Form):
    QUESTION_CHOICES = [
        ('Answer 5', 'Answer 5'),
        ('Answer 6', 'Answer 6'),
        ('Answer 7', 'Answer 7'),
        ('Answer 8', 'Answer 8'),
    ]

    question_two_select = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )


class QuizOneQuestionThree(forms.Form):
    QUESTION_CHOICES = [
        ('Answer 9', 'Answer 9'),
        ('Answer 10', 'Answer 10'),
        ('Answer 11', 'Answer 11'),
        ('Answer 12', 'Answer 12'),
    ]

    question_three_select = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )