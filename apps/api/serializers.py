from django.contrib.auth.models import User
from rest_framework import serializers

from apps.polls.models import Test, Testrun


class TestSerializer(serializers.HyperlinkedModelSerializer):
    pub_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Test
        fields = ['test_text', 'test_description', 'pub_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['email', 'username']


class TestrunSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    finished_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Testrun
        fields = ['user', 'finished_at']


class TestWithRunsCountSerializer(serializers.HyperlinkedModelSerializer):
    count_of_runs = serializers.SerializerMethodField(read_only=True)
    pub_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Test
        fields = ['test_text', 'test_description', 'pub_date', 'count_of_runs']

    def get_count_of_runs(self, obj):
        return obj.test_runs.count()
