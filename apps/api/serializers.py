from rest_framework import serializers

from apps.polls.models import Test


class TestSerializer(serializers.HyperlinkedModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Test
        fields = ['test_text', 'test_description', 'pub_date']

