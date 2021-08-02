from django.utils import timezone
from django.views import generic

from .models import Test


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


class ResultsView(generic.DetailView):
    model = Test
    template_name = 'polls/results.html'


def run_test(request, test_id):
    print(test_id)