from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Test(models.Model):
    test_text = models.CharField(max_length=200)
    test_description = models.CharField(max_length=600)
    questions = models.ManyToManyField(Question)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.test_text


class Testrun(models.Model):
    test = models.ForeignKey(Test, related_name="test_runs",
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                             default=None, null=True)
    finished_at = models.DateTimeField(auto_now_add=True)


class TestrunQuestion(models.Model):
    testrun = models.ForeignKey(Testrun, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300)
