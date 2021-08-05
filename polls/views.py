from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic, View

from .forms import TestrunQuestionModelForm
from .models import Test, Testrun, TestrunQuestion


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
        TestrunQuestionFormSet = modelformset_factory(
            TestrunQuestion,
            form=TestrunQuestionModelForm,
            extra=amount,
            max_num=amount,
        )
        context = {
            "test": test,
            "formset": TestrunQuestionFormSet(
                queryset=TestrunQuestion.objects.none(),
                initial=[{"question": item.question_text} for item in questions],
            )
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        test = get_object_or_404(Test, pk=pk)
        questions = test.questions.all()
        amount = questions.count()
        formset = TestrunFormQuestionSet = modelformset_factory(
            TestrunQuestion,
            form=TestrunQuestionModelForm,
            extra=amount,
            max_num=amount,
        )(request.POST)
        if formset.is_valid():
            testrun = Testrun.objects.create(test_id=pk)
            instances = formset.save(commit=False)
            for instance in instances:
                instance.testrun = testrun
            TestrunQuestion.objects.bulk_create(instances)
            return redirect("polls:index")

