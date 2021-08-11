from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View

from .forms import TestrunQuestionModelForm
from .models import Test, Testrun, TestrunQuestion


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_tests_list'
    queryset = Test.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login'
    model = Test
    template_name = 'polls/detail.html'
    context_object_name = 'test'


class TestrunView(LoginRequiredMixin, View):
    login_url = '/accounts/login'
    template_name = 'polls/testrun.html'

    def get_user(self, request):
        if request.user.is_authenticated:
            return request.user
        return None

    def get_test_question_formset(self, amount):
        return modelformset_factory(
            TestrunQuestion,
            form=TestrunQuestionModelForm,
            extra=amount,
            max_num=amount,
        )

    def get(self, request, pk):
        test = get_object_or_404(Test, pk=pk)
        questions = test.questions.all()
        amount = questions.count()
        TestrunQuestionFormSet = self.get_test_question_formset(amount)
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
        formset = self.get_test_question_formset(amount)(request.POST)
        if formset.is_valid():
            testrun = Testrun.objects.create(test_id=pk, user=self.get_user(request))
            instances = formset.save(commit=False)
            for instance in instances:
                instance.testrun = testrun
            TestrunQuestion.objects.bulk_create(instances)
            return redirect("polls:index")

