from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic, View

from .forms import TestrunModelForm
from .models import Test, Testrun


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_tests_list'
    queryset = Test.objects.all()


class DetailView(generic.DetailView):
    model = Test
    template_name = 'polls/detail.html'
    context_object_name = 'test'


class TestrunView(View):
    template_name = 'polls/testrun.html'

    def get(self, request, pk):
        test = get_object_or_404(Test, pk=pk)
        questions = test.questions.all()
        amount = questions.count()
        TestrunFormSet = modelformset_factory(
            Testrun,
            form=TestrunModelForm,
            extra=amount,
            max_num=amount,
        )
        context = {
            "test": test,
            "formset": TestrunFormSet(
                initial=[{"question": question} for question in questions],
            )
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        test = get_object_or_404(Test, pk=pk)
        questions = test.questions.all()
        amount = questions.count()
        formset = TestrunFormSet = modelformset_factory(
            Testrun,
            form=TestrunModelForm,
            extra=amount,
            max_num=amount,
        )(request.POST)
        print(formset.cleaned_data)

