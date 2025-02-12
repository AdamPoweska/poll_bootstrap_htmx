from django import forms

class QuizOneQuestionOne(forms.Form):
    QUESTION_CHOICES = [
        ('Answer 1 - Free coffee', 'Answer 1 - Free coffee'),
        ('Answer 2 - I can sit on a chair', 'Answer 2 - I can sit on a chair'),
        ('Answer 3 - I have company laptop', 'Answer 3 - I have company laptop'),
        ('Answer 4 - I do not have to work in rain', 'Answer 4 - I do not have to work in rain'),
    ]

    question_one_select = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )


class QuizOneQuestionTwo(forms.Form):
    QUESTION_CHOICES = [
        ('Answer 5 - Salary', 'Answer 5 - Salary'),
        ('Answer 6 - Fruit Thrusday', 'Answer 6 - Fruit Thrusday'),
        ('Answer 7 - Great mood in workplace', 'Answer 7 - Great mood in workplace'),
        ('Answer 8 - Feeling of doing important work', 'Answer 8 - Feeling of doing important work'),
    ]

    question_two_select = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )


class QuizOneQuestionThree(forms.Form):
    QUESTION_CHOICES = [
        ('Answer 9 - Nothing, company is perfect', 'Answer 9 - Nothing, company is perfect'),
        ('Answer 10 - Please give me more work and do not increase my pay', 'Answer 10 - Please give me more work and do not increase my pay'),
        ('Answer 11 - More integrations events', 'Answer 11 - More integrations events'),
        ('Answer 12 - Please increase my pay', 'Answer 12 - Please increase my pay'),
    ]

    question_three_select = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )

