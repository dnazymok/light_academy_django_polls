from django.forms import modelformset_factory
from django.shortcuts import render
from django.utils import timezone
from django.views import generic, View

from .models import Test, Testrun
from .forms import TestrunModelForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_tests_list'

    def get_queryset(self):
        return Test.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Test
    template_name = 'polls/detail.html'
    context_object_name = 'test'


class TestrunView(View):
    def get(self, request, pk):
        test = Test.objects.get(pk=pk)
        questions = test.questions.all()
        amount = questions.count()
        TestrunFormSet = modelformset_factory(
            Testrun,
            form=TestrunModelForm,
            extra=amount,
            max_num=amount
        )
        context = {
            "test": test,
            'formset': TestrunFormSet(
                queryset=Testrun.objects.none(),
                initial=[{"question": question} for question in questions],
            )
        }
        return render(
            request,
            "polls/testrun.html",
            context=context,
        )

