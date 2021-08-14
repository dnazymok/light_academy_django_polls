from django_filters import rest_framework as filters

from apps.polls.models import Test


class TestFilter(filters.FilterSet):
    min_date = filters.IsoDateTimeFilter(field_name="pub_date", lookup_expr='gte')
    max_date = filters.IsoDateTimeFilter(field_name="pub_date", lookup_expr='lte')

    class Meta:
        model = Test
        fields = ['pub_date']