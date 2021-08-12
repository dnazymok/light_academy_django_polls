from django.urls import path, include
from rest_framework import routers

from apps.api.views import TestListView, TestDetailView, TestrunListView, \
    TestWithRunsCountListView, TestWithTopThreeRunsCountListView

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("tests/", TestListView.as_view(), name="tests"),
    path("tests/<int:pk>", TestDetailView.as_view(), name="test_detail"),
    path("tests/with_runs_count/", TestWithRunsCountListView.as_view(),
         name="tests_with_runs_count"),
    path("tests/top_three/", TestWithTopThreeRunsCountListView.as_view(),
         name="tests_top_three"),
    path("testruns/", TestrunListView.as_view(), name="testruns"),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
]
