from django import forms

from apps.polls.models import Question, TestrunQuestion


class TestrunQuestionModelForm(forms.ModelForm):
    question = forms.ModelChoiceField(
        label="",
        queryset=Question.objects.all(),
        to_field_name="question_text",
        widget=forms.TextInput(
            attrs={"class": "form-control", "readonly": "readonly"}
        ),
    )
    answer = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "required": True}
        ),
    )

    class Meta:
        model = TestrunQuestion
        fields = ("question", "answer",)
