from django.urls import path, include
from rest_framework import routers

from apps.api.views import TestListView, TestDetailView

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("tests/", TestListView.as_view(), name="tests"),
    path("tests/<int:pk>", TestDetailView.as_view(), name="test_detail"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]