from django import forms

from polls.models import Question, Testrun


class TestrunModelForm(forms.ModelForm):
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
        model = Testrun
        fields = ("question", "answer",)
