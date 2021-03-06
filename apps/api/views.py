from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from rest_framework.generics import GenericAPIView

from apps.api.filters import TestFilter
from apps.api.serializers import TestSerializer, TestrunSerializer, \
    TestWithRunsCountSerializer
from apps.polls.models import Test, Testrun


class TestListView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   GenericAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TestFilter
    ordering_fields = ['test_text', 'pub_date']
    search_fields = ['test_text', 'test_description']


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TestDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TestrunListView(mixins.ListModelMixin,
                      GenericAPIView):
    queryset = Testrun.objects.all()
    serializer_class = TestrunSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TestWithRunsCountListView(mixins.ListModelMixin,
                                GenericAPIView):
    queryset = Test.objects.all()
    serializer_class = TestWithRunsCountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TestWithTopThreeRunsCountListView(mixins.ListModelMixin,
                                        GenericAPIView):
    queryset = Test.objects.annotate(count=Count('test_runs')).order_by(
        '-count')[:3]
    serializer_class = TestWithRunsCountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
